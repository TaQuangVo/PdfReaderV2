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

def Decide_output(isins, depoInst):

    # Validate ISINs
    invalid_isins = []
    for isin in isins:
        if not FindIsinFromList(isin['isin'], isin.get('valuta'), ALLOWED_ISINS):
            invalid_isins.append(isin)
    
    is_valid = len(invalid_isins) == 0

    if len(isins) == 0 or depoInst is None:
        return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "is_valid": is_valid,
            "invalid_isin_list": invalid_isins,
            "email": OUTCOME_EMAIL_TEMPLATE["AS_tom"]
        }


    # Send to AS
    if not is_valid and depoInst == "Strivo":
        return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "is_valid": is_valid,
            "invalid_isin_list": invalid_isins,
            "email": OUTCOME_EMAIL_TEMPLATE["AS_ej_godkand"]
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
    
    return {
            "found_isins": isins,
            "depo_inst": depoInst,
            "email": OUTCOME_EMAIL_TEMPLATE[email_key]
        }