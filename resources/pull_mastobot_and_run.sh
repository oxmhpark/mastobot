#!/bin/bash

# 설정값
IMAGE="ghcr.io/oxmhpark/mastobot:latest"
CONTAINER_NAME="mastobot-container"

# 환경 변수 (필요 시 수정)
export GITHUB_REPO_OWNER="your-github-username"
export GITHUB_REPO_NAME="your-repo-name"
export GITHUB_REPO_ROOT="docs"  # 루트면 빈 문자열 ""
export MASTODON_BASE_URL="https://your.instance"
export MASTODON_ACCESS_TOKEN="your-access-token"

# 1. 최신 이미지 가져오기
echo "📦 Pulling latest image..."
docker pull "$IMAGE"

# 2. 기존 컨테이너가 있다면 중지 및 삭제
if docker ps -a --format '{{.Names}}' | grep -q "^$CONTAINER_NAME$"; then
  echo "🛑 Stopping and removing existing container..."
  docker stop "$CONTAINER_NAME"
  docker rm "$CONTAINER_NAME"
fi

# 3. 새 컨테이너 실행
echo "🚀 Running new container..."
docker run --name "$CONTAINER_NAME" -d \
  -e GITHUB_REPO_OWNER \
  -e GITHUB_REPO_NAME \
  -e GITHUB_REPO_ROOT \
  -e MASTODON_BASE_URL \
  -e MASTODON_ACCESS_TOKEN \
  "$IMAGE"

echo "✅ Done."
