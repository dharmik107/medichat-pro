from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = " "
    for page in reader.pages:
        text += page.extract_text() or "  "
    return text