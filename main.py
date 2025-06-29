from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from core.config import get_settings
from core.logger import logger
from routers import all_routes
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

settings = get_settings()

logger = logger.bind(trace_id="N/A")

app = FastAPI(title="DATA_TO_EXCEL", version="0.1.0")

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.mount("/css", StaticFiles(directory="view/css"), name="css")

templates = Jinja2Templates(directory="view")

for router_instance in all_routes:
    app.include_router(router_instance)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
