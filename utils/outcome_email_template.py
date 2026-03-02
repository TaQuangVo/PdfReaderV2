garantum_mail = ""
AS_mail = ""
strivo_mail = ""
nordnet_mail = ""
mfex_mail = ""
fg_mail = ""
test_mail = "daniel.karoumi@sakra.se"

standard_message = (
    "Hej,<br><br>"
    "Se bifogat signerat dokument.<br><br>"
    "För att kontrollera dokumentet klicka här:<br>"
    '<a href="https://www.leosys.se/?page=proxy.bankid.validera">Kontrollera Bank-ID signerat dokument</a><br><br>'
    "OBS: Signatur-ID och tidpunkt behöver inte anges då ni laddar upp bifogad PDF för kontroll.<br><br>"
    "Hälsningar Säkra VP AB"
)

OUTCOME_EMAIL_TEMPLATE = {
    "AS_tom_inga_isins": {
        "template_name": "AS_tom_inga_isins",
        "message": "Inga värdepapper hittades i blanketten. Manuell granskning krävs.",
        "email_to": AS_mail+";"+test_mail,
    },
    "AS_tom_ingen_depo": {
        "template_name": "AS_tom_ingen_depo",
        "message": "Depåinstitut saknas eller kunde inte identifieras. Manuell granskning krävs.",
        "email_to": AS_mail+";"+test_mail,
    },
    "AS_ej_godkand": {
        "template_name": "AS_ej_godkand",
        "message": "Flytt ej godkänd.",
        "email_to": AS_mail+";"+test_mail,
    },
    "nordnet_special": {
        "template_name": "nordnet_special",
        "message": standard_message,
        "email_to": fg_mail+";"+nordnet_mail+";"+test_mail,
    },
    "nordnet_fund": {
        "template_name": "nordnet_fund",
        "message": standard_message,
        "email_to": mfex_mail+";"+fg_mail+";"+nordnet_mail+";"+test_mail,
    },
    "strivo_special": {
        "template_name": "strivo_special",
        "message": standard_message,
        "email_to": fg_mail+";"+strivo_mail+";"+test_mail,
    },
    "strivo_fund": {
        "template_name": "strivo_fund",
        "message": standard_message,
        "email_to": mfex_mail+";"+fg_mail+";"+strivo_mail+";"+test_mail,
    },
    "garantum_special": {
        "template_name": "garantum_special",
        "message": standard_message,
        "email_to": fg_mail+";"+garantum_mail+";"+test_mail,
    },
    "garantum_fund": {
        "template_name": "garantum_fund",
        "message": standard_message,
        "email_to": mfex_mail+";"+fg_mail+";"+garantum_mail+";"+test_mail,
    },
}
