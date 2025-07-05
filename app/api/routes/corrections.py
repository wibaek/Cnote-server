from fastapi import APIRouter
import uuid

from app.api.models.request import CorrectionRequest
from app.api.models.response import CorrectionResponse
from app.services.correction import correct_text

router = APIRouter()


@router.post("/", response_model=CorrectionResponse)
def post_correction(payload: CorrectionRequest):
    return CorrectionResponse(
        id=str(uuid.uuid4()),
        raw_text=payload.raw_text,
        corrected_text=correct_text(payload.raw_text),
    )


@router.get("/{correction_id}", response_model=CorrectionResponse)
def get_correction(correction_id: str):
    return CorrectionResponse(
        id=correction_id,
        raw_text="오늘은 날씨가 맑스니다.",
        corrected_text="오늘은 날씨가 맑습니다.",
    )
