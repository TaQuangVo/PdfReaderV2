import re
from PyPDF2 import PdfReader
from pathlib import Path
from collections import defaultdict
from docling.document_converter import DocumentConverter
ISIN_RE = re.compile(r"\b[A-Z]{2}[A-Z0-9]{9}[0-9]\b")

def match_row_data(data):
    pattern = re.compile(r"vardepapper_(\d+)_(namn|isin|valuta)")
    grouped = []

    for item in data:
        match = pattern.match(item["/T"])
        if match and not (item.get("/V") == ''):
            index, field = match.groups()
            index = int(index) - 1  # zero-based index

            # Ensure the list is long enough
            while len(grouped) <= index:
                grouped.append({})

            grouped[index][field] = item["/V"]

    return grouped

def printPDFWithDocling(pdf_path):
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    markdown = result.document.export_to_markdown()
    print(markdown)

def printbasic(file_path):
    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        print(f"\n--- Page {page_number} ---\n")
        print(text)

def extract_isins_from_form_fields(pdf_path):
    reader = PdfReader(pdf_path)
    fields = reader.get_fields() or {}

    array = []
    for name, field in fields.items():
        array.append(field)

    data = match_row_data(array)
    
    return {
        "data":data,
        "inst": "hello"
    }

def extractFundFromPdf(pdf_path): 
    reader = PdfReader(pdf_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Regex pattern:
    # - Fund name: greedy text until ISIN
    # - ISIN: standard ISIN format
    # - Currency: SEK, USD, EUR (extend if needed)
    pattern = re.compile(
        r"""
        (?P<name>.*?)                    # Fund name
        \s+
        (?P<isin>[A-Z]{2}[A-Z0-9]{10})   # ISIN
        (?:\s+(?P<currency>SEK|USD|EUR))?  # Optional currency
        """,
        re.VERBOSE
    )

    results = []

    for match in pattern.finditer(text):
        results.append({
            "namn": match.group("name").strip(),
            "isin": match.group("isin"),
            "valuta": match.group("currency")
        })

    found_strivo = re.search(r'(?m)^\s*Strivo\s*$', text) != None

    return {
        "isinList": results,
        "depoInst": "Strivo" if found_strivo else "unknown"
    }

if __name__ == "__main__":
    pdf_file = "files/Flyttblankett Strivo approved.pdf"
    #result = extract_isins_from_form_fields(pdf_file)

    #printPDFWithDocling(pdf_file)
    result = extractFundFromPdf(pdf_file)
    print(result)
    #printbasic(pdf_file)

    #print(result)
