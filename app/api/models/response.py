from pydantic import BaseModel


class CorrectionResponse(BaseModel):
    id: str
    raw_text: str
    corrected_text: str
