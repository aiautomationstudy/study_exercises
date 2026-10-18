# 로드맵 제작·게시·검증 기록

독자용 문서는 상위 폴더의 Markdown 16편이다. 이 파일은 제작·유지보수 기록이며 독자용 목차에 포함하지 않는다.

## 요청과 구성

- AI 시대의 개발자 레벨·직급을 중심으로 성장의 책임과 전환을 설명한다.
- 영상의 E3~E7을 뼈대로 쓰되 공식 Meta 인사 기준으로 제시하지 않는다.
- 배경에 따른 독자 구분을 두지 않고, AI로 제품을 만드는 출발점부터 참고할 수 있게 쓴다.
- 각 레벨의 역할·기대 결과·증거·AI 활용·정체·다음 과제를 제공한다.
- 창업은 기술 레벨과 연결해 연습하되 직급 환산으로 쓰지 않는다.
- 영상의 전체 자막은 공개 저장소에 포함하지 않는다. 한국어 수동 자막 1,064개 구간을 추출해 읽고 시간대로 인용했다.
- 원자료·연구 조건·자료의 해석·가상 예시·학습 제안을 구분한다.

## 파일과 재생성

- 정본: 상위 폴더의 `README.md`, `01-*.md`~`15-*.md`.
- 웹: Markdown과 동일한 본문을 사전 변환한 HTML 16개. 문서 링크는 HTML 대상으로 변환한다.
- 부가 기능: 레벨별 빠른 이동, 제목 검색, 문서 목차, 이전·다음, 원문 다운로드, 양식 복사.
- 외부 스크립트·CDN·분석 도구·서버 API 없음. JavaScript가 없어도 본문과 링크를 읽을 수 있다.
- 스타일·보조 기능: `assets/style.css`, `assets/site.js`.
- 생성: `tools/build.py`, 빌드 의존성은 `tools/requirements.txt`에 고정했다.

저장소 루트에서 실행:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r ai-developer-roadmap/tools/requirements.txt
.venv/bin/python ai-developer-roadmap/tools/build.py
python3 ai-developer-roadmap/tools/verify.py
node --check ai-developer-roadmap/assets/site.js
git diff --check
```

가상환경 `.venv/`은 기존 저장소 규칙에 따라 커밋하지 않는다. 설치 위치를 달리해도 결과는 같다.

## 게시 방식

- 저장소: `aiautomationstudy/study_exercises`.
- 착수 시 Pages 설정을 API로 재확인: legacy, `main`, `/`.
- 기존 `.nojekyll` 유지. HTML과 Markdown 원문을 함께 커밋해 push한다.
- 공개 주소: https://aiautomationstudy.github.io/study_exercises/ai-developer-roadmap/
- 복구가 필요하면 이 작업의 변경을 되돌리는 새 커밋을 main에 반영한다. 기존 강의 자료와 로컬 설정은 수정하지 않는다.

## 검증 상태

### 로컬 확인 · 2026-10-18

- 정본 Markdown 16편, 공백 포함 53,455자. HTML 16개 생성 성공.
- `python3 ai-developer-roadmap/tools/verify.py`: 내부 파일·목차 링크 596개, 중복 ID 없음, 페이지당 h1·main 각각 1개, 원문 대응 확인.
- `node --check ai-developer-roadmap/assets/site.js`: 통과.
- Playwright 격리 Chromium: 16개 페이지 × 화면 너비 1,440·390·320px = 48회 열기. HTTP 200, 제목·탐색·본문 확인, 페이지 가로 넘침 없음, JavaScript 실행 오류 없음.
- 문서 제목 검색(E5·결과 없음·초기화), 레벨 카드 이동, 문서 목차 이동, 모바일 메뉴·검색·이동 확인.
- 양식 복사: 클립보드와 원문 코드 블록의 내용 일치. Markdown 다운로드: 로컬 원문의 바이트와 일치.
- 모바일 표 좌우 스크롤, JavaScript를 끈 상태의 본문·탐색 확인.
- 데스크톱·모바일 화면 캡처를 육안 확인. 표는 모바일에서 영역 안에서 좌우 스크롤한다.
- 참고 링크 31개 직접 HTTP 확인 모두 200. YouTube는 페이지 조회 없이 지정 추출기로 자막 확인.
- 새 텍스트 파일의 주요 자격증명 패턴 검사: 탐지 없음. 비밀값이 전혀 없다는 보증으로 확대하지 않는다.
- 전용 단위 테스트·린트 설정이 없는 정적 문서 묶음이다. 필요한 빌드·링크·문법·실제 브라우저 검증을 수행했다.

### 공개 게시

- 본문 배포 커밋 `161f8c9d196e26843ad7fb551e1c64845c220497`을 main에 push하고, 같은 커밋의 Pages 빌드 `built`를 API로 확인했다.
- 공개 HTML 16개·Markdown 원문 16개·CSS/JS 2개, 총 34개 모두 HTTPS 200과 로컬 파일의 SHA-256 일치를 확인했다.
- 공개 Pages에서 Playwright 격리 Chromium으로 HTML 16개 × 너비 1,440·390px = 32회 확인. 페이지 가로 넘침·JavaScript 실행 오류 없음.
- 공개 페이지의 레벨 카드·목차·제목 검색·문서 이동·모바일 메뉴·표 스크롤 확인.
- 공개 페이지의 양식 복사와 원문 다운로드도 각각 내용·바이트 일치 확인.
- 구조화한 실제 결과와 34개 파일의 해시는 [verification.json](verification.json)에 남겼다. 해당 결과는 본문 배포 커밋의 검증이며 후속 기록 커밋은 독자용 본문을 바꾸지 않는다.
- 로컬 시험 서버를 종료하고 해당 포트의 접속 종료를 확인했다. 시험용 브라우저는 각 실행에서 닫았다.

### 변경·작업본 점검

- 변경 범위는 새 `ai-developer-roadmap/` 폴더와 루트 README의 안내 링크 추가이다. 기존 강의 자료는 수정하지 않았다.
- 검사나 테스트를 약화시킨 변경 없음. 재생성한 HTML 16개의 바이트가 동일해 빌드 재현성 확인.
- `git diff --check` 통과. 기존 로컬 설정 `.serena/`는 배포에 포함하지 않았다.
- 사용 저장소는 이 저장소 하나이며, 작업본은 원래의 main 1개이다. 임시 worktree 생성·제거 각각 0개. 원래 main은 계속 사용하는 작업본이므로 유지한다.
- 판정: 독자용 자료 구현·로컬 검증·공개 게시·공개 브라우저 검증 완료. 독자의 학습 효과나 실제 직급 평가는 이 검증 범위에 포함하지 않는다.
