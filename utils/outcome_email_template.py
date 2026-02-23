garantum_mail = ""
AS_mail = ""
strivo_mail = ""
nordnet_mail = ""
mfex_mail = ""
fg_mail = ""
test_mail = "daniel.karoumi@sakra.se"

OUTCOME_EMAIL_TEMPLATE = {
    "AS_tom": {
        "template_name": "AS_tom",
        "message": "Tom flyttblanket. Inga värdepapper hittades. Manuell granskning krävs.",
        "email_to": AS_mail+";"+test_mail, # send to AS and test mail
        "subject": "Tom flyttblanket"
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