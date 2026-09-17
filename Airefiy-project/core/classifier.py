import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

class CredibilityClassifier:
    """
    Supervised classification engine for Airefiy. 
    Trains and executes a machine learning model to classify academic 
    abstracts based on text patterns and linguistic features.
    """
    
    def __init__(self, model_path: str = "artifacts/credibility_model.pkl"):
        self.model_path = model_path
        # Pipeline combining TF-IDF vectorization and a robust Logistic Regression classifier
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2), stop_words='english')),
            ('clf', LogisticRegression(max_iter=1000, C=1.0))
        ])
        self.is_trained = False

    def train(self, X_train: list, y_train: list):
        """
        Trains the classification model using a list of text samples 
        and corresponding labels (1 for Credible/Rigorous, 0 for Low Credibility/Sensational).
        """
        if not X_train or not y_train:
            raise ValueError("Training data cannot be empty.")
        
        print("Training Airefiy classification pipeline...")
        self.pipeline.fit(X_train, y_train)
        self.is_trained = True
        print("Model training completed successfully.")

    def evaluate(self, X_test: list, y_test: list) -> dict:
        """Evaluates model performance on a test set."""
        if not self.is_trained:
            raise Exception("Model is not trained yet. Call train() or load_model() first.")
        
        predictions = self.pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions, output_dict=True)
        
        return {
            "accuracy": round(accuracy, 4),
            "detailed_report": report
        }

    def predict_credibility(self, text: str) -> dict:
        """
        Predicts the credibility class and computes a confidence probability score 
        (acting as the core Credibility Index).
        """
        if not self.is_trained:
            # Attempt to load a pre-trained model artifact if available
            if os.path.exists(self.model_path):
                self.load_model()
            else:
                raise Exception("No trained model found. Please train the model or provide a saved artifact.")

        # Get probability estimates [probability of class 0, probability of class 1]
        probabilities = self.pipeline.predict_proba([text])[0]
        prediction = self.pipeline.predict([text])[0]
        
        # Calculate a 0-100 Credibility Index based on the probability of being credible (class 1)
        credibility_index = round(float(probabilities[1]) * 100, 2)

        return {
            "predicted_class": int(prediction),
            "status": "Reliable / Rigorous" if prediction == 1 else "Flagged / Low Rigor",
            "credibility_index": credibility_index,
            "confidence_scores": {
                "low_credibility_prob": round(float(probabilities[0]), 4),
                "high_credibility_prob": round(float(probabilities[1]), 4)
            }
        }

    def save_model(self):
        """Saves the trained model pipeline to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.pipeline, self.model_path)
        print(f"Model successfully saved to {self.model_path}")

    def load_model(self):
        """Loads a pre-trained model pipeline from disk."""
        if os.path.exists(self.model_path):
            self.pipeline = joblib.load(self.model_path)
            self.is_trained = True
            print(f"Model loaded successfully from {self.model_path}")
        else:
            raise FileNotFoundError(f"Model file not found at {self.model_path}")