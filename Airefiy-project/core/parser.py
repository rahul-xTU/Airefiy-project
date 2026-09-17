import re
import io
from pypdf import PdfReader
from docx import Document

class AcademicTextParser:
    """
    Custom text parser module for Airefiy. 
    Handles text cleaning, boilerplate removal, and direct text extraction 
    from uploaded PDF and Word (.docx) files.
    """
    
    def __init__(self):
        self.boilerplate_patterns = [
            r'arXiv:\d{4}\.\d{4,5}(v\d+)?\s*\[[a-zA-Z\-]+\]',  # arXiv stamps
            r'Page \d+ of \d+',                              # Page numbers
            r'©\s*\d{4}.*?(?=\n|$)',                         # Copyright notices
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' # Raw URLs
        ]

    def extract_text_from_file(self, uploaded_file) -> str:
        """
        Detects file type (PDF or DOCX) and extracts raw text string 
        from the uploaded Streamlit file object.
        """
        file_extension = uploaded_file.name.split('.')[-1].lower()
        extracted_text = ""

        try:
            if file_extension == 'pdf':
                reader = PdfReader(uploaded_file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"
                        
            elif file_extension in ['docx', 'doc']:
                doc = Document(uploaded_file)
                for paragraph in doc.paragraphs:
                    if paragraph.text.strip():
                        extracted_text += paragraph.text + "\n"
            else:
                return "Unsupported file format. Please upload a PDF or Word document."
        except Exception as e:
            return f"Error reading file: {str(e)}"

        return extracted_text

    def remove_boilerplate(self, text: str) -> str:
        """Strips headers, footers, URLs, and pre-print tracking tags."""
        if not text:
            return ""
        
        cleaned = text
        for pattern in self.boilerplate_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        return cleaned

    def clean_text(self, text: str) -> str:
        """Normalizes whitespace and cleans raw text strings."""
        if not isinstance(text, str):
            return ""
        
        text = self.remove_boilerplate(text)
        text = re.sub(r'[\r\n\t]+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def extract_structural_signals(self, text: str) -> dict:
        """Extracts quick heuristic indicators for empirical backing."""
        cleaned_text = self.clean_text(text)
        
        has_metrics = bool(re.search(r'\b\d+(\.\d+)?%|\b\d+\s*(fold|percent|samples|participants|epochs|accuracy)\b', cleaned_text, re.IGNORECASE))
        has_citations = bool(re.search(r'\[\d+(?:,\s*\d+)*\]|\([A-Za-z]+\s+et al\.,\s*\d{4}\)', cleaned_text))

        return {
            "processed_text": cleaned_text,
            "word_count": len(cleaned_text.split()),
            "contains_quantitative_metrics": has_metrics,
            "contains_citations": has_citations
        }