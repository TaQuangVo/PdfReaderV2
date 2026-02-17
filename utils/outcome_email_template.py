garantum_mail = ""
AS_mail = ""
strivo_mail = ""
nordnet_mail = ""
mfex_mail = ""
fg_mail = ""

OUTCOME_EMAIL_TEMPLATE = {
    "AS_tom": {
        "template_name": "AS_tom",
        "message": "Tom flyttblanket. Inga ISIN hittades. Manuell granskning krävs.",
        "email_to": AS_mail, # send to AS
        "subject": "Tom flyttblanket"
    },
    "AS_ej_godkand": {
        "template_name": "AS_ej_godkand",
        "message": "Flytt ej godkänd.",
        "email_to": AS_mail, # send to AS
        "subject": "EJ godkänt flyttblanket"
    },
    "nordnet_special": {
        "template_name": "nordnet_special",
        "message": "Flyttblankett",
        "email_to": fg_mail+";"+nordnet_mail,
        "subject": "Flyttblankett"
    },
    "nordnet_fund": {
        "template_name": "nordnet_fund",
        "message": "Flyttblankett",
        "email_to": mfex_mail+";"+fg_mail+";"+nordnet_mail,
        "subject": "Flyttblankett"
    },
    "strivo_special": {
        "template_name": "strivo_special",
        "message": "Flyttblankett",
        "email_to": fg_mail+";"+strivo_mail,
        "subject": "Flyttblankett"
    },
    "strivo_fund": {
        "template_name": "strivo_fund",
        "message": "Flyttblankett",
        "email_to": mfex_mail+";"+fg_mail+";"+strivo_mail,
        "subject": "Flyttblankett"
    },
    "garantum_special": {
        "template_name": "garantum_special",
        "message": "Flyttblankett",
        "email_to": fg_mail+";"+garantum_mail,
        "subject": "Flyttblankett"
    },
    "garantum_fund": {
        "template_name": "garantum_fund",
        "message": "Flyttblankett",
        "email_to": mfex_mail+";"+fg_mail+";"+garantum_mail,
        "subject": "Flyttblankett"
    },
}