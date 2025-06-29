from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Request
from core.logger import logger
from controller import parse_pdf
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="view")

router = APIRouter(
    prefix="/pdf_parser",
    tags=["pdf_parser"]
)

@router.post("/upload")
async def upload_pdf(request: Request, pdf_file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {pdf_file.filename}")

        # Step 1: Parse the file
        parsed_text = parse_pdf(pdf_file)
        #
        # # Step 2: Upload the file to Supabase
        # pdf_file.file.seek(0)  # rewind file for re-read
        # supabase_url = await upload_pdf_to_supabase(pdf_file)
        #
        # logger.info(f"File uploaded to Supabase: {supabase_url}")

        return {
            "message": "PDF parsed and uploaded successfully",
            "text": parsed_text
        }
    except Exception as e:
        logger.error(f"PDF processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))