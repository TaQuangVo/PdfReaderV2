import base64
import io

def Get_pdf_stream_from_resquest(req):
# Try to get base64 encoded PDF from JSON body (for Logic Apps)
    try:
        req_body = req.get_json()
        pdf_base64 = req_body.get('file') or req_body.get('pdfContent')

        if pdf_base64:
            # Decode base64 to binary
            pdf_binary = base64.b64decode(pdf_base64)
        else:
            raise ValueError("No PDF content found in JSON body.")
    except ValueError:
        # Fallback to multipart/form-data (for Postman)
        pdf_file = req.files.get('file')
        if not pdf_file:
            raise ValueError("No PDF file found in form-data.")
        pdf_binary = pdf_file.read()

    # Create in-memory file object
    pdf_stream = io.BytesIO(pdf_binary)

    return pdf_stream