from fastapi import APIRouter

from app.api.routes import audios, corrections

router = APIRouter()
router.include_router(corrections.router, tags=["correction"], prefix="/v1/corrections")
router.include_router(audios.router, tags=["audio"], prefix="/v1/audios")
