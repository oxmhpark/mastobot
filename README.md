# mastobot

공개된 Github 저장소의 대상 폴더로부터 마크다운(`.md`) 파일들을 읽고 무작위 1개를 지정된 Mastodon 인스턴스에 포스팅하는 봇.

## 환경변수 (필수)

|	변수 이름				|	설명															|
|---------------------------|-------------------------------------------------------------------|
|	`GITHUB_REPO_OWNER`		|	Github 저장소 소유자 이름										|
|	`GITHUB_REPO_NAME`		|	Github 저장소 이름												|
|	`GITHUB_REPO_ROOT`		|	마크다운 파일이 위치한 저장소 내 경로 (루트 폴더면 빈 문자열)	|
|	`MASTODON_BASE_URL`		|	Mastodon 인스턴스 URL (예: https://mastodon.social)				|
|	`MASTODON_ACCESS_TOKEN`	|	Mastodon 인스턴스 액세스 토큰									|

## 봇 실행 예시

### 1. 스크립트 사용자화 및 저장

👉 [pull_mastobot_and_run.sh](./resources/pull_mastobot_and_run.sh)

### 2. 스크립트 실행권한 부여

```shell
chmod +x ./pull_mastobot_and_run.sh
```

### 3. 스크립트 실행

```bash
./pull_mastobot_and_run.sh
```

## cron 설정 예시

매일 새벽 3시에 최신 이미지 pull 후 컨테이너 재시작

```bash
0 3 * * * /path/to/pull_mastobot_and_run.sh >> /var/log/mastobot.log 2>&1
```