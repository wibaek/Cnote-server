from api.routes.api import router as api_router
from core.config import DEBUG, PROJECT_NAME, VERSION
from fastapi import FastAPI


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router)
    return application


app = get_application()
