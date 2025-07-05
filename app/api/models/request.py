from pydantic import BaseModel


class CorrectionRequest(BaseModel):
    raw_text: str
