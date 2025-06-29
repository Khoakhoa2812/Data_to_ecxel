import fitz  # PyMuPDF
from fastapi import UploadFile
import tempfile
import uuid
from core import logger
from utils import clean_pdf_text
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="view")


def parse_pdf(file: UploadFile):
    try:
        logger.info(f"Received file: {file.filename}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.file.read())
            tmp_path = tmp.name

        logger.debug(f"Temporary file saved at: {tmp_path}")

        doc = fitz.open(tmp_path)
        full_text = "\n".join([page.get_text("text") for page in doc])
        doc.close()

        logger.info(f"Extracted text length: {len(full_text)} characters")
        return templates.TemplateResponse("excel_export.html")

    except Exception as e:
        logger.exception(f"PDF processing failed: {e}")
        raise




