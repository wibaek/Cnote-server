from fastapi import APIRouter

from api.routes import corrections

router = APIRouter()
router.include_router(corrections.router, tags=["correction"], prefix="/v1/corrections")
