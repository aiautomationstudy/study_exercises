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

로컬 확인과 구분해 Pages 빌드·HTTPS·실제 브라우저 결과를 게시 후 기록한다.
