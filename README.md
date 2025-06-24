# mastobot

공개된 깃헙 저장소의 대상 폴더로부터 마크다운(`.md`) 파일들을 읽고 무작위 1개를 지정된 마스토돈 인스턴스에 포스팅하는 봇.

# 환경변수 (필수)

|	변수 이름	|	설명	|
|--|--|
|	`GITHUB_REPO_OWNER`	|	깃헙 저장소 소유자 이름	|
|	`GITHUB_REPO_NAME`	|	깃헙 저장소 이름	|
|	`GITHUB_REPO_ROOT`	|	마크다운 파일이 위치한 저장소 내 경로 (루트 폴더면 빈 문자열)	|
|	`MASTODON_BASE_URL`	|	마스토돈 인스턴스 URL (예: https://mastodon.social)	|
|	`MASTODON_ACCESS_TOKEN`	|	마스토돈 액세스 토큰	|

# cron 설정 예시

매일 새벽 3시에 최신 이미지 pull 후 컨테이너 재시작

```bash
0 3 * * * docker pull ghcr.io/oxmhpark/mastobot:latest && \
docker stop CONTAINER_NAME && docker rm CONTAINER_NAME && \
docker run --name CONTAINER_NAME -d \
  -e GITHUB_REPO_OWNER=GITHUB_USER \
  -e GITHUB_REPO_NAME=GITHUB_REPO_NAME \
  -e GITHUB_REPO_ROOT=GITHUB_REPO_ROOT \
  -e MASTODON_BASE_URL=MASTODON_URL \
  -e MASTODON_ACCESS_TOKEN=MASTODON_TOKEN \
  ghcr.io/oxmhpark/mastobot:latest
```