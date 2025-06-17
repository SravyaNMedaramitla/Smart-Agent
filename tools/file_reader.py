# tools/file_reader.py

import fitz
import pytesseract
from pdf2image import convert_from_path
import os

# Set path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sravy\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def read_file(file_path):
    if file_path.endswith(".txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading .txt file: {str(e)}"

    elif file_path.endswith(".pdf"):
        try:
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()

            if text.strip():
                return text
            else:
                print("⚠️ No text found via PyMuPDF — switching to OCR.")
                return ocr_pdf(file_path)

        except Exception as e:
            return f"Error reading .pdf file: {str(e)}"
    else:
        return "Unsupported file type. Please upload a .txt or .pdf file."

def ocr_pdf(file_path):
    try:
        print("🔍 Performing OCR on PDF...")
        pages = convert_from_path(file_path)
        full_text = ""
        for i, img in enumerate(pages):
            text = pytesseract.image_to_string(img)
            full_text += f"\n--- Page {i+1} ---\n{text}"
        return full_text.strip() if full_text else "OCR couldn't extract text."
    except Exception as e:
        return f"OCR Error: {str(e)}"
