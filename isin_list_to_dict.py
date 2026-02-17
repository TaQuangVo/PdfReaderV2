import json

from utils.allowed_isins_list import ALLOWED_ISINS

def parse_isins(isin_list):
    result = {}

    for item in isin_list:
        if len(item) > 12:  # ISIN is always 12 chars
            isin = item[:12]
            currency = item[12:]
        else:
            isin = item
            currency = None

        result[isin] = {"currency": currency}

    return result


isin_dict = parse_isins(ALLOWED_ISINS)
with open("alow_isin_dict.json", "w", encoding="utf-8") as f:
    json.dump(isin_dict, f, indent=2)

print("File written: alow_isin_dict.json")