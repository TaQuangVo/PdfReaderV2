import re
ISIN_RE = re.compile(r"\b[A-Z]{2}[A-Z0-9]{9}[0-9]\b")
AVAILABLE_CURRENCIES = {"SEK", "USD", "EUR", "JPY", "NOK"}

def extractFundFromCUResult(cu_result: dict):
    """
    Extract fund rows and depo institution from Content Understanding (CU) result JSON.

    Returns same structure as extractFundFromPdf():
    {
        "isinList": [{"namn": str, "isin": str, "valuta": str|None}, ...],
        "depoInst": "Strivo" | "Nordnet" | "Garantum" | None
    }
    """

    def _get_field_value(fields: dict, key: str) -> str | None:
        if not isinstance(fields, dict):
            return None
        obj = fields.get(key)
        if not isinstance(obj, dict):
            return None

        # Common CU shapes: valueString / value
        return obj.get("valueString") or obj.get("value")

    def _clean_isin(x: str | None) -> str | None:
        if not x:
            return None
        # Remove spaces and other separators, keep alnum, uppercase
        cleaned = re.sub(r"[^A-Za-z0-9]", "", x).upper()
        # Must be 12 chars for ISIN
        if len(cleaned) != 12:
            return None
        # Optionally validate against your ISIN regex
        if not ISIN_RE.match(cleaned):
            return None
        return cleaned

    def _clean_currency(x: str | None) -> str | None:
        if not x:
            return None
        cur = re.sub(r"[^A-Za-z]", "", x).upper()
        if cur in AVAILABLE_CURRENCIES:
            return cur
        return "Unknown" 

    # CU root can be either the full payload (with "result") or directly "result"
    result = cu_result.get("result", cu_result)
    contents = result.get("contents") or []

    if not contents or not isinstance(contents, list):
        return {"isinList": [], "depoInst": None}

    # You currently have one document in contents; use the first
    doc = contents[0] if isinstance(contents[0], dict) else {}
    fields = doc.get("fields") or {}

    # Depo institution
    depo_raw = _get_field_value(fields, "TransferringInstitutionName")
    depoInst = None
    if depo_raw:
        d = depo_raw.strip()
        # Normalize common variants/case
        if d.lower() == "nordnet":
            depoInst = "Nordnet"
        elif d.lower() == "strivo":
            depoInst = "Strivo"
        elif d.lower() == "garantum":
            depoInst = "Garantum"

    # Assets array -> funds
    isinList = []
    assets = fields.get("Assets", {})
    valueArray = assets.get("valueArray") if isinstance(assets, dict) else None

    if isinstance(valueArray, list):
        for item in valueArray:
            if not isinstance(item, dict):
                continue
            valueObject = None

            # CU commonly stores objects like {"type":"object","valueObject":{...}}
            if "valueObject" in item and isinstance(item["valueObject"], dict):
                valueObject = item["valueObject"]
            # Sometimes it may already be the object
            elif item.get("type") == "object" and isinstance(item.get("value"), dict):
                valueObject = item["value"]

            if not isinstance(valueObject, dict):
                continue

            name = _get_field_value(valueObject, "AssetName")
            isin = _clean_isin(_get_field_value(valueObject, "Isin"))
            cur = _clean_currency(_get_field_value(valueObject, "Currency"))

            # Only include entries with a valid ISIN (so endpoint behaves consistently)
            if isin:
                isinList.append({
                    "namn": (name or "").strip(),
                    "isin": isin,
                    "valuta": cur
                })

    return {"isinList": isinList, "depoInst": depoInst}

import json
from pathlib import Path

def main():
    # Path to the CU JSON file (adjust as needed)
    json_path = Path("mock.json")

    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path.resolve()}")

    with json_path.open("r", encoding="utf-8") as f:
        cu_payload = json.load(f)

    extracted = extractFundFromCUResult(cu_payload)

    print("---- Extracted from CU ----")
    print(f"depoInst: {extracted.get('depoInst')}")
    print(f"fund count: {len(extracted.get('isinList', []))}")
    print(json.dumps(extracted, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
