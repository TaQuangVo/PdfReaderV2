garantum_mail = "garantum_testmail"
AS_mail = "AS_testmail"
strivo_mail = "Strivo_testmail"
nordnet_mail = "Nordnet_testmail"
mfex_mail = "MFEX_testmail"
fg_mail = "FG_testmail"
test_mail = "daniel.karoumi@sakra.se"

OUTCOME_EMAIL_TEMPLATE = {
    "AS_tom_inga_isins": {
        "template_name": "AS_tom_inga_isins",
        "message": "Inga värdepapper hittades i blanketten. Manuell granskning krävs.",
        "email_to": AS_mail+";"+test_mail,
        "subject": "Inkorrekt flyttblanket"
    },
    "AS_tom_ingen_depo": {
        "template_name": "AS_tom_ingen_depo",
        "message": "Depåinstitut saknas eller kunde inte identifieras. Manuell granskning krävs.",
        "email_to": AS_mail+";"+test_mail,
        "subject": "Inkorrekt flyttblanket"
    },
    "AS_ej_godkand": {
        "template_name": "AS_ej_godkand",
        "message": "Flytt ej godkänd.",
        "email_to": AS_mail+";"+test_mail, # send to AS and test mail
        "subject": "Ej godkänd flyttblanket"
    },
    "nordnet_special": {
        "template_name": "nordnet_special",
        "message": "Flyttblankett med special-ISIN",
        "email_to": fg_mail+";"+nordnet_mail+";"+test_mail,
        "subject": "Flyttblankett med special-ISIN"
    },
    "nordnet_fund": {
        "template_name": "nordnet_fund",
        "message": "Flyttblankett fonder",
        "email_to": mfex_mail+";"+fg_mail+";"+nordnet_mail+";"+test_mail,
        "subject": "Flyttblankett fonder"
    },
    "strivo_special": {
        "template_name": "strivo_special",
        "message": "Flyttblankett med special-ISIN",
        "email_to": fg_mail+";"+strivo_mail+";"+test_mail,
        "subject": "Flyttblankett med special-ISIN"
    },
    "strivo_fund": {
        "template_name": "strivo_fund",
        "message": "Flyttblankett fonder",
        "email_to": mfex_mail+";"+fg_mail+";"+strivo_mail+";"+test_mail,
        "subject": "Flyttblankett fonder"
    },
    "garantum_special": {
        "template_name": "garantum_special",
        "message": "Flyttblankett med special-ISIN",
        "email_to": fg_mail+";"+garantum_mail+";"+test_mail,
        "subject": "Flyttblankett med special-ISIN"
    },
    "garantum_fund": {
        "template_name": "garantum_fund",
        "message": "Flyttblankett fonder",
        "email_to": mfex_mail+";"+fg_mail+";"+garantum_mail+";"+test_mail,
        "subject": "Flyttblankett fonder"
    },
}