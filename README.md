# Airefiy: Academic Pre-Print & Research Claim Credibility Analyzer

## Overview
**Airefiy** is an advanced Natural Language Processing (NLP) and supervised machine learning application designed to evaluate academic research abstracts, pre-prints, and project reports. The system processes unstructured document text, strips tracking boilerplate, extracts custom linguistic and empirical markers, and computes an objective **Credibility Index** to assist students and researchers in auditing literature reliability.

This project was developed as part of the coursework evaluation for **CSA2001: Fundamentals in AI and ML**.

---

## Key Features
* **Multi-Format Document Ingestion:** Automatically extracts raw text from uploaded PDF research papers and Word (`.docx`) documents.
* **Linguistic Heuristic Analyzer:** Scans text against custom lexical dictionaries to quantify empirical methodologies versus sensationalized or exaggerated claims.
* **Supervised Classification Engine:** Utilizes a trained `scikit-learn` Logistic Regression pipeline combined with TF-IDF vectorization to classify academic rigor.
* **Interactive Analytics Dashboard:** Built with Streamlit to display real-time metrics, structural signals, and JSON payload exports.

---

## Technologies & Tools Used
* **Python 3.10+** (Core programming language)
* **Streamlit** (Interactive web application framework)
* **Scikit-Learn** (Supervised machine learning classification & TF-IDF vectorization)
* **PyPDF & Python-Docx** (Document text extraction libraries)
* **Joblib & NumPy** (Model serialization and numerical arrays)
* **Git & GitHub** (Version control and project submission)

---

## System Architecture & Folder Structure
```text
Airefiy-project/
│
├── artifacts/             # Serialized model checkpoints (.pkl files)
├── core/                  # Modular backend logic
│   ├── __init__.py
│   ├── parser.py          # Document text extraction & cleaning
│   ├── feature_weights.py # Empirical vs. sensational lexicon analysis
│   ├── classifier.py      # Scikit-learn classification engine
│   └── pipeline.py        # End-to-end master orchestration workflow
│
├── interface.py           # Streamlit user interface dashboard
├── requirements.txt       # Project dependencies list
├── statement.md           # Formal project scope definition
└── README.md              # Project documentation
```

---

## Installation & Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone or Open the Repository:**
   Navigate into your project root directory via your terminal (`Airefiy-project`).

2. **Install Dependencies:**
   Run the following command to install all required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application:**
   Launch the web dashboard locally using Python:
   ```bash
   python -m streamlit run interface.py
   ```

---

## Testing Instructions

1. Once the Streamlit interface opens in your web browser, use the file uploader widget.
2. Select an academic PDF research paper or Word document (`.docx`).
3. View the extracted text preview if desired, then click **"Run Credibility Analysis on Document"**.
4. Review the generated **Credibility Index (0–100)**, classification status, empirical lexicon matches, and structural signal tabs.
5. Use the sidebar button to reset or retrain the baseline model pipeline if needed.
