# mastobot

지정된 GitHub 저장소의 대상 폴더로부터 마크다운(`.md`) 파일들을 읽어, 무작위로 1개를 선택해 Mastodon 인스턴스에 게시하는 봇.

## 환경변수 (필수)

|	변수 이름				|	설명															|
|---------------------------|-------------------------------------------------------------------|
|	`GITHUB_REPO_OWNER`		|	GitHub 저장소 소유자 이름										|
|	`GITHUB_REPO_NAME`		|	GitHub 저장소 이름												|
|	`GITHUB_REPO_ROOT`		|	마크다운 파일이 위치한 저장소 내 경로 (루트 폴더면 빈 문자열)	|
|	`MASTODON_BASE_URL`		|	Mastodon 인스턴스 URL (예: https://mastodon.social)				|
|	`MASTODON_ACCESS_TOKEN`	|	Mastodon 인스턴스 액세스 토큰									|

## 봇 실행 방법

이 저장소를 클론한 후, 다음 중 하나의 방법을 선택해서 실행한다.

### ✅ GitHub Actions 활용

> GitHub Actions 기능으로 `mastobot.py` 스크립트를 반복실행하므로 서버나 Docker 환경이 필요없다.

#### 1. 예약실행 워크플로 설정

- `.github/workflows/cron.yaml.sample`의 이름을 `.github/workflows/cron.yaml`으로 변경한다.
- `cron.yaml` 파일을 수정해서 실행 간격을 설정한다.

#### 2. 환경변수 등록

`저장소 > Settings > Secrets and variables` 메뉴에서 원하는 값을 입력한다.

#### 3. 자동실행 확인

GitHub Actions 탭에서 예약 실행 결과를 확인한다.

### 🐳 Docker를 이용한 로컬 실행

> Docker가 설치된 서버가 필요하다.

#### 1. 패키지 빌드 워크플로 설정

- `.github/workflows/publish.yaml.sample`의 이름을 `.github/workflows/publish.yaml`으로 변경한다.
- 커밋하면 Docker 이미지가 자동으로 빌드된다.

#### 2. 스크립트 사용자화 및 저장

- 👉 [pull_mastobot_and_run.sh](./resources/pull_mastobot_and_run.sh) 파일을 서버에 업로드한다.
- 업로드한 `pull_mastobot_and_run.sh` 파일을 열어 환경변수를 수정한다.

#### 3. 스크립트 실행권한 부여

```shell
chmod +x ./pull_mastobot_and_run.sh
```

#### 4. 스크립트 실행

```bash
./pull_mastobot_and_run.sh
```

#### 5. cron 설정 예시

매일 새벽 3시에 최신 이미지 pull 후 컨테이너 재시작

```bash
0 3 * * * /path/to/pull_mastobot_and_run.sh >> /var/log/mastobot.log 2>&1
```