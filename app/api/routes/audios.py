from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import uuid
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "./uploads/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class AudioUploadResponse(BaseModel):
    id: str


@router.post("/", response_model=AudioUploadResponse)
async def upload_audio(file: UploadFile = File(...)):
    if file.content_type not in ["audio/wav", "audio/mpeg", "audio/mp3"]:
        raise HTTPException(status_code=400, detail="지원하지 않는 파일 형식입니다.")

    if not file.filename:
        raise HTTPException(status_code=400, detail="파일 이름이 필요합니다.")
    ext = os.path.splitext(file.filename)[-1] or ".wav"  # 기본 확장자

    file_id = str(uuid.uuid4())
    filename = f"audio_{file_id}{ext}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return AudioUploadResponse(id=file_id)
