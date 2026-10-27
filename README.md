# study_exercises

## AI 시대 개발자 성장 로드맵

[웹에서 읽기 — E3 Junior에서 E7 Senior Staff까지](https://aiautomationstudy.github.io/study_exercises/ai-developer-roadmap/)

개발자 레벨과 직급에 따라 문제의 범위·기대 성과·다음 단계 준비가 어떻게 달라지는지 정리한 16편의 가이드입니다.
자기 진단, 레벨별 실습, AI 협업, 기술 기반, 창업 경로, 실행 계획과 기록 양식을 제공합니다.
영상의 커리어 회고와 기업의 공개 성장 기준·연구를 바탕으로 작성했으며, 회사별 공식 승진 기준과는 구분합니다.
[Markdown 원문과 전체 목차](ai-developer-roadmap/README.md) · [출처](ai-developer-roadmap/15-sources.md)

## AI 자동화 스터디 3기

[기본실습 — AI에게 브라우저 일 맡기기](https://aiautomationstudy.github.io/study_exercises/3기/실습/3기_3주차_사전준비+실습_AI에게_브라우저_일_맡기기.html)

서울숲 안내문 한 장을 만들고 글씨를 크게 고치는 순서로 따라 합니다. 붙여넣는 위치와 단계별 완료 확인을 안내하며, 기존 예제·설치·설정은 필요할 때 펼쳐 봅니다.
[쉬운 안내서 원문](3기/실습/3기_기본실습_AI에게_브라우저_일_맡기기.md)

[기본실습 — 내 지침으로 블로그 포스팅 자동화하기](https://aiautomationstudy.github.io/study_exercises/3기/실습/3기_기본실습_내_지침으로_블로그_포스팅_자동화하기.html)

본인 기준에 맞는 글 한 편을 읽고 고쳐 저장하는 순서로 따라 합니다. 블로그가 없어도 시작할 수 있습니다. 공개 발행과 GitHub 보관·두 블로그 운영·검색·광고는 필요한 단계부터 이어갑니다.
[안내서 원문](3기/실습/3기_기본실습_내_지침으로_블로그_포스팅_자동화하기.md)

[심화실습 #4 — 나만의 위키 만들기](https://aiautomationstudy.github.io/study_exercises/3기/실습/3기_심화실습_4_나만의_위키_만들기.html)

한글(HWP·HWPX)·Word·엑셀·웹페이지·YouTube 자료를 주제별로 연결하고, 원문 근거로 질문하며, 새 자료를 더하는 개인 위키 실습입니다. 페이지의 「문장 복사」로 바로 따라 할 수 있습니다.
[안내서 원문](3기/실습/3기_심화실습_4_나만의_위키_만들기.md)

[4주차 실습 막힘 해결 안내서](https://aiautomationstudy.github.io/study_exercises/3기/실습/3기_4주차_실습하다_막혔을때_해결안내.html)

컴퓨터를 잘 모르는 참가자가 Codex에 해결을 맡길 문장을 복사할 수 있습니다.
정본 Markdown은 `3기/실습/3기_4주차_실습하다_막혔을때_해결안내.md`입니다.

## 동국대 AI 특강

2회차(10월 15일): [내 웹앱 만들기 실습 안내](https://aiautomationstudy.github.io/study_exercises/동국대/학사_특강/2회차_웹앱만들기_실습안내.html)

Gemini·ChatGPT·Claude에게 Antigravity용 요청문 작성을 맡기고, 작은 웹앱을 제작·확인·수정하는 개인 실습입니다.
[안내서 원문](동국대/학사_특강/2회차_웹앱만들기_실습안내.md), [학습 진도 완성 예시](https://aiautomationstudy.github.io/study_exercises/동국대/학사_특강/2회차_학습진도_완성예시.html)를 함께 제공합니다.

[실습 자료 모아 보기](https://aiautomationstudy.github.io/study_exercises/동국대/학사_특강/)

`동국대/학사_특강/index.html`에서 학생 사전준비 안내, 실습 프롬프트(Pro·Plus), 퀴즈 예시 2종,
녹음 비서 과제 안내, Antigravity 사용 한도 안내, 자동화 아이디어 30선을 열 수 있습니다.

### 배포와 수정

- GitHub Pages는 기존 설정인 `main` 브랜치의 저장소 루트(`/`)에서 배포합니다.
- `.nojekyll`을 유지하여 HTML을 그대로 제공합니다. 별도의 빌드나 설치는 필요 없습니다.
- HTML을 수정하고 `main`에 push하면 GitHub Pages가 자동으로 갱신됩니다.
- 파일 이름을 바꾸면 자료 목록과 다른 문서의 상대 링크도 함께 수정하세요.
- `퀴즈_완성예시.html`은 기존 동국대 강의 자료의 `발표자료_v4/실습/퀴즈_완성예시.html`에서 가져왔습니다.
- `03_학생_사전준비안내.html`은 같은 강의 자료의 `학생안내/03_학생_사전준비안내.html`을 원본 그대로 복사했습니다.

### 공개 배포 검증 (2026-10-08)

- 자료 배포 커밋: `3cb1f789cb77102ebc701ccf67c84b0cba950102`. Pages 빌드 완료를 API로 확인했습니다.
- 목록 포함 HTML 8개: 공개 HTTPS 응답 모두 200, 서버 파일과 로컬 파일의 SHA-256 일치.
- 내부 링크·목차 85개: 대상 파일과 문서 내 이동 위치 존재 확인.
- Playwright 격리 Chromium: 목록에서 자료 7개로 이동, Pro·Plus 프롬프트 복사 확인.
- 완성 퀴즈: 미선택 안내, 3문항 정답·점수, 다시 풀기 확인.
- 목록 화면: 너비 390px·1280px에서 가로 넘침 없음. 모바일 캡처 육안 확인.
- HTML 8개를 열 때 JavaScript 실행 오류 없음. 문제 찾기 예시의 학습용 동작은 원본 그대로 제공.
- 별도의 빌드·테스트·린트 설정이 없는 정적 자료 저장소이며, `git diff --check` 통과.
- 작업본 정리: 임시 worktree 제거 0개, 현재 `main` 작업본 1개 유지. 기존 `.serena/` 로컬 설정은 배포 대상에서 제외.

### 학생 사전준비 안내 추가 검증 (2026-10-08)

- 목록의 맨 위에 「실습 전 준비 → 학생 사전준비 안내」를 추가해 자료 8개를 제공합니다.
- 새 안내 HTML과 원본 파일의 바이트 일치, 전체 HTML 9개의 내부 링크·목차 116개 확인.
- 로컬 HTTP 서버와 Playwright 격리 Chromium에서 목록 링크 8개, 사전준비 안내 이동·복사 버튼 검증.
- 안내 페이지 너비 390px·1280px에서 가로 넘침과 JavaScript 실행 오류 없음. `git diff --check` 통과.
