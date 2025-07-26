from docx import Document

def extract_text_from_docx(docx_file):
    try:
        doc = Document(docx_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"❌ Error reading DOCX file: {str(e)}"
