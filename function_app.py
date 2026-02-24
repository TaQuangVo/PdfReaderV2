import azure.functions as func
import logging
import json
import re

from utils.extract_fund_from_CU_result import extractFundFromCUResult
from utils.extract_fund_from_pdf import extractFundFromPdf
from utils.decide_output import Decide_output
from utils.pdf_stream_from_request import Get_pdf_stream_from_resquest

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="validate-isins", methods=["POST"])
def validate_isins(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing PDF ISIN validation request.')

    try:
        try:
            pdf_stream = Get_pdf_stream_from_resquest(req)
        except Exception as e:
            logging.error(f"Error extracting PDF stream: {str(e)}")
            return func.HttpResponse(
                f"Error extracting PDF stream: {str(e)}",
                status_code=400
            )

        # Extract ISINs
        result = extractFundFromPdf(pdf_stream)
        isins = result["isinList"]
        depoInst = result["depoInst"]

        output = Decide_output(isins, depoInst)

        depanr = None
        email_body = req.params.get("email_body")
        if email_body:
            match = re.search(r'Dep[åa]nr[:\s]*(\S+)', email_body, re.IGNORECASE)
            if match:
                depanr = match.group(1)
        if depanr:
            output["email"]["subject"] = f"{output['email']['subject']} - {depanr}"

        return func.HttpResponse(
            body=json.dumps(output),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error processing PDF: {str(e)}")
        return func.HttpResponse(
            f"Error processing PDF: {str(e)}",
            status_code=500
        )


@app.route(route="validate-isins-CU", methods=["POST"])
def validate_isins_CU(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing PDF ISIN validation request.')

    try:
        req_body = req.get_json()

        # Extract ISINs
        result = extractFundFromCUResult(req_body)
        isins = result["isinList"]
        depoInst = result["depoInst"]

        output = Decide_output(isins, depoInst)
        
        return func.HttpResponse(
            body=json.dumps(output),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error processing PDF: {str(e)}")
        return func.HttpResponse(
            f"Error processing PDF: {str(e)}",
            status_code=500
        )
