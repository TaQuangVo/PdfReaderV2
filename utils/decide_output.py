import os
from utils.allowed_isins_list import ALLOWED_ISINS
from utils.special_isins import SPECIAL_ISINS
from utils.outcome_email_template import OUTCOME_EMAIL_TEMPLATE

def FindIsinFromList(isin: str, valuta: str|None, list_to_match) -> bool:
    """
        Determin if isin is in allowed list \n
        if currency is given for both isin and the current matching item in allowed list, both must match \n
        return True as soon as a match is found
    """
    valuta = "" if valuta is None else valuta
    isinvaluta = isin+valuta
    for s in list_to_match:
        if len(s) == 12 or len(isinvaluta) == 12:
            if s[:12] == isin[:12]:
                return True
 
        else:
            if s == isinvaluta:
                return True
    return False

def Build_message(base_message, isins, depoInst):
    isin_lines = "\n".join(
        f"- {i['isin']}" + (f" ({i['valuta']})" if i.get('valuta') else "")
        for i in isins
    )
    parts = [base_message, f"Depåinstitut: {depoInst}" if depoInst else "", isin_lines]
    return "\n".join(p for p in parts if p)

def Decide_output(isins, depoInst):

    skip_validation = os.environ.get("SKIP_ISIN_VALIDATION", "false").lower() == "true"

    # Validate ISINs
    invalid_isins = []
    if not skip_validation:
        for isin in isins:
            if not FindIsinFromList(isin['isin'], isin.get('valuta'), ALLOWED_ISINS):
                invalid_isins.append(isin)

    is_valid = len(invalid_isins) == 0

    if len(isins) == 0 or depoInst is None:
        template = OUTCOME_EMAIL_TEMPLATE["AS_tom"]
        return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "is_valid": is_valid,
            "invalid_isin_list": invalid_isins,
            "email": {**template, "message": Build_message(template["message"], isins, depoInst)}
        }


    # Send to AS
    if not is_valid and depoInst == "Strivo":
        template = OUTCOME_EMAIL_TEMPLATE["AS_ej_godkand"]
        return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "is_valid": is_valid,
            "invalid_isin_list": invalid_isins,
            "email": {**template, "message": Build_message(template["message"], isins, depoInst)}
        }

    specialIsinsFound = []
    for isin in isins:
        if FindIsinFromList(isin['isin'], isin.get('valuta'), SPECIAL_ISINS):
            specialIsinsFound.append(isin)
    containSpecialIsins = len(specialIsinsFound) > 0

    if containSpecialIsins:
        email_key = f"{depoInst.lower()}_special"
    else:
        email_key = f"{depoInst.lower()}_fund"

    template = OUTCOME_EMAIL_TEMPLATE[email_key]
    return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "email": {**template, "message": Build_message(template["message"], isins, depoInst)}
        }