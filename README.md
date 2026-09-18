## Overview
Airefiy uses advanced Natural Language Processing and supervised machine learning to check the credibility of academic abstracts, pre-prints, and research project reports. It reads unstructured text from your documents, strips out generic boilerplates, pulls out custom linguistic and empirical markers, and then calculates a Credibility Index. This gives students and researchers a straightforward way to judge whether a piece of literature is reliable.


This project was developed as part of the coursework evaluation for **CSA2001: Fundamentals in AI and ML**.

---

## Key Features
Multi-Format Document Ingestion: Upload a PDF or Word (.docx) research paper—Airefiy automatically grabs the raw text for you.

Linguistic Heuristic Analyzer: Scans your document against custom dictionaries to pick up on the difference between solid research methods and over-the-top or exaggerated claims.

Supervised Classification Engine: Uses a trained scikit-learn Logistic Regression pipeline with TF-IDF vectorization to rate academic rigor.

Interactive Analytics Dashboard: Built in Streamlit, this dashboard shows real-time metrics, signals in the document’s structure, and lets you export results in JSON.

---

## Technologies & Tools Used
Python 3.10+ (core programming language)
Streamlit (for the interactive web UI)
Scikit-Learn (for machine learning and TF-IDF)
PyPDF & Python-Docx (to pull text from documents)
Joblib & NumPy (for model saving and numerical ops)
Git & GitHub (version control, project hand-in)
Project Structure
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


## Results
<img width="1917" height="1140" alt="Screenshot 2026-09-18 211519" src="https://github.com/user-attachments/assets/cf473c8c-21a1-4680-81d8-d98eb73108f5" />


## Testing Instructions

1. Once the Streamlit interface opens in your web browser, use the file uploader widget.
2. Select an academic PDF research paper or Word document (`.docx`).
3. View the extracted text preview if desired, then click **"Run Credibility Analysis on Document"**.
4. Review the generated **Credibility Index (0–100)**, classification status, empirical lexicon matches, and structural signal tabs.
5. Use the sidebar button to reset or retrain the baseline model pipeline if needed.
