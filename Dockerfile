# 베이스 이미지 선택 (경량 Python 환경)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 코드 복사
COPY mastobot.py .

# 실행 명령 (스크립트를 바로 실행)
CMD ["python", "mastobot.py"]