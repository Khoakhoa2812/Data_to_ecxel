from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Request
from core.logger import logger
from controller import parse_pdf
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="view")

router = APIRouter(
    prefix="/pdf_process",
    tags=["pdf_process"]
)

