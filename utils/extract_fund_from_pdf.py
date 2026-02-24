from PyPDF2 import PdfReader
import re
import logging

ISIN_RE = re.compile(r"\b[A-Z]{2}[A-Z0-9]{9}[0-9]\b")

def extractFundFromPdf(file): 
    """
    read fundflytt pdf file and return
    :param file: file-like object (binary mode)
    :return: {
            "isinList": [
                {
                    "namn": "Fund Name",
                    "isin": "ISINCODE",
                    "valuta": "USD"
                }
            ],
            "depoInst": "Strivo" or "Nordnet" or "Garantum" or None
    }
    """
    reader = PdfReader(file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    # logging.info(f"Extracted PDF text:\n{text}")

    # Regex pattern:
    # - Fund name: greedy text until ISIN
    # - ISIN: standard ISIN format
    # - Currency: SEK, USD, EUR (extend if needed)
    pattern = re.compile(
        r"""
        (?P<name>.*?)                    # Fund name
        \s+
        (?P<isin>[A-Z]{2}[A-Z0-9]{10})   # ISIN
        (?:\s+(?P<currency>USD|SEK|EUR|JPY|NOK))?  # Optional currency USD|SEK|EUR|JPY|NOK
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

    depInst = re.search(r'(?m)^\s*(?:Strivo|Nordnet|Garantum)\s*$', text)
    depInst = depInst.group(0).strip() if depInst else None


    return {
        "isinList": results,
        "depoInst": depInst
    }