# Project Statement: Airefiy

## 1. Problem Statement
In the modern academic and research ecosystem, the rapid proliferation of pre-prints and online literature makes it challenging to quickly evaluate the empirical rigor and methodological validity of research documents. Manual vetting is time-consuming, and low-quality or sensationalized claims can easily be overlooked. There is a need for an automated, objective screening tool that evaluates academic documents based on textual structure and linguistic patterns.

## 2. Project Scope
**Airefiy** is a Natural Language Processing (NLP) and supervised machine learning web application designed to ingest unstructured academic documents (PDF and Word `.docx`), clean tracking boilerplate, extract custom linguistic and empirical markers, and evaluate text credibility using a supervised classification model.

## 3. Target Users
* **Students & Researchers:** To quickly audit literature reliability and check the academic tone of drafts or pre-prints.
* **Academic Reviewers & Evaluators:** To assist in preliminary screening of document structure and empirical backing.

## 4. High-Level Features
* **Multi-Format Document Ingestion:** Extracts raw text automatically from PDF and Word (.docx) files.
* **Linguistic Heuristic Analysis:** Quantifies empirical terminology versus sensationalized/hype terminology.
* **Supervised Machine Learning Classification:** Employs a scikit-learn Logistic Regression pipeline with TF-IDF vectorization.
* **Interactive Analytics Interface:** Built via Streamlit to display real-time credibility indices, structural signal breakdowns, and exportable JSON reports.
