# Cnote-server

FastAPI 기반의 텍스트 및 음성 보정 API 서버입니다.

---

## 🛠️ 초기 설정 가이드

### 1. `uv` 설치 (패키지 매니저)

> `uv`는 pip + virtualenv 대체 도구로, 빠르고 가볍습니다.

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

### 2. 가상환경 생성 및 패키지 설치

```
uv venv
source .venv/bin/activate  # macOS / Linux

uv sync # pyproject.toml 기반의 경우
```

### 3. 실행 방법

```
uv run uvicorn app.main:app --reload
```

- 서버 실행: http://localhost:8000
- Swagger 문서: http://localhost:8000/docs
