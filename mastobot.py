# mastodon_bot.py

import os
import requests
import random
import re
from mastodon import Mastodon

# 1. GitHub 저장소 정보
GITHUB_REPO = "https://api.github.com/repos/{owner}/{repo}/contents/{path}"
GITHUB_REPO_OWNER = os.environ["GITHUB_REPO_OWNER"]
GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME"]
GITHUB_REPO_ROOT = os.getenv("GITHUB_REPO_ROOT", "")  # 기본값은 루트("")

# 2. 마스토돈 인증 정보
MASTODON_BASE_URL = os.environ["MASTODON_BASE_URL"]  # 예: https://mastodon.social
MASTODON_ACCESS_TOKEN = os.environ["MASTODON_ACCESS_TOKEN"]

# 3. GitHub에서 .md 파일 목록 가져오기
def fetch_markdown_files():
    url = GITHUB_REPO.format(owner=GITHUB_REPO_OWNER, repo=GITHUB_REPO_NAME, path=GITHUB_REPO_ROOT)
    res = requests.get(url)
    res.raise_for_status()

    files = res.json()
    md_files = [f for f in files if f["name"].endswith(".md")]
    return md_files

# 4. 콘텐츠 가져오기
def fetch_file_content(file_info):
    raw_url = file_info["download_url"]
    res = requests.get(raw_url)
    res.raise_for_status()
    return res.text

# 5. 포맷팅
def filter_markdown_syntax(markdown_content):
    return re.sub(r'^#+\s*', '', markdown_content, flags=re.MULTILINE).strip()

# 6. 길이 조절
def adjust_content_length(full_length_content, source_url):
    max_len = 500

    # 길이 제한에 걸리지 않는다면 그대로 속행
    if len(full_length_content) <= max_len:
        return full_length_content

    link_text = f" …\n\n{source_url}"

    # 원문에서 첫 500자 추출
    first_500 = full_length_content[:max_len]

    # 1단계: 첫 500자 안에 줄바꿈이 존재하면 거기서 자름
    newline_pos = first_500.rfind('\n')
    trimmed = first_500[:newline_pos].rstrip()
    if len(trimmed) + len(link_text) <= max_len:
        return f"{trimmed}{link_text}"

    # 2단계: 줄바꿈 없으면 글자 수 기준으로 자름
    else:
        allowed_len = max_len - len(link_text)
        trimmed = full_length_content[:allowed_len].rstrip()
        return f"{trimmed}{link_text}"

# 7. 마스토돈에 게시
def post_to_mastodon(markdown_content, source_url):
    mastodon = Mastodon(
        access_token=MASTODON_ACCESS_TOKEN,
        api_base_url=MASTODON_BASE_URL
    )
    filtered_content = filter_markdown_syntax(markdown_content)
    toot = adjust_content_length(filtered_content, source_url)

    try:
        mastodon.toot(toot)
    except Exception as e:
        print(f"❌ Mastodon post failed: {e}")

# 8. 실행 함수
def main():
    print("📥 Fetching markdown files...")
    files = fetch_markdown_files()
    if not files:
        print("❌ No markdown files found.")
        return

    random.seed()
    chosen = random.choice(files)
    print(f"📄 Selected: {chosen['name']}")

    content = fetch_file_content(chosen)
    post_to_mastodon(content, chosen["download_url"])
    print("✅ Posted to Mastodon!")

if __name__ == "__main__":
    main()
