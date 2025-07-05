from fastapi import APIRouter
import uuid

from api.models.request import CorrectionRequest
from api.models.response import CorrectionResponse
from services.correction import correct_text

router = APIRouter()


@router.post("/", response_model=CorrectionResponse)
def post_correction(payload: CorrectionRequest):
    return CorrectionResponse(
        id=str(uuid.uuid4()),
        raw_text=payload.raw_text,
        corrected_text=correct_text(payload.raw_text),
    )
