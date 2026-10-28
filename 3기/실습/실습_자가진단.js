'use strict';
// 증상은 진단 결과가 아니다. 상태를 읽고 확인하도록 안내하며 자동 설치·실행하지 않는다.
const selfCheckCases = {
  chat: {
    next: '대화가 안 되면 쓰던 문장을 메모에 보관하고 ChatGPT.com에서 오류 화면을 보여 주세요. 앱과 모델 이름을 임의로 바꾸거나 반복 재설치하지 않습니다.',
    anchor: 'chat',
    prompt: 'ChatGPT 앱(Codex)이 켜지지 않거나 대화가 안 돼.\n아래 오류와 이미 해 본 방법을 보고 다음 한 가지 행동을 알려줘.\n앱·모델의 현재 지원 여부와 실제 오류를 확인하고 원인을 단정하지 마.\n대화가 가능해지면 원래 실습 폴더에서 이어가게 해줘.'
  },
  computer: {
    next: '앱의 Plugins에서 Computer Use 설치·활성화를 확인하세요. Mac의 화면 기록·손쉬운 사용 권한과 앱별 접근 허용은 각각 확인합니다. Windows는 대상 앱이 보이는 활성 데스크톱에서 동작합니다.',
    anchor: 'computer-use',
    prompt: '현재 앱과 운영체제에서 컴퓨터 유즈를 쓸 수 있는지 확인해줘.\n공식 OpenAI 안내와 실제 Plugins·Computer use 설정을 확인하고 이미 설치된 것은 재사용해줘.\nMac이면 화면 기록·손쉬운 사용 권한과 앱별 접근을 따로 확인해줘.\nWindows면 대상 앱이 활성 데스크톱에 보이는지 확인해줘.\n전체 액세스만 켜면 모두 해결된다고 하지 마.\n내가 지정한 앱에서 허용한 작업만 확인하고, 실제로 읽은 화면으로 성공을 검증해줘.'
  },
  cli: {
    next: 'Aside 브라우저, 명령 도구(CLI), Codex가 읽는 aside-browser 스킬을 따로 확인합니다. 창이 열린 것과 Codex 연결 완료는 다릅니다.',
    anchor: 'aside-cli',
    prompt: 'Aside 창은 있는데 명령 또는 aside-browser 스킬을 못 찾는다고 해.\n브라우저·CLI·Codex 스킬의 설치 위치와 버전을 각각 확인해줘.\n이미 설치된 것은 보존하고 현재 공식 안내가 지원하는 경로로만 복구해줘.\naside skills list와 Codex의 스킬 목록은 다르니 실제 SKILL.md 인식·읽기를 확인해줘.\n마지막으로 이 실습 대화에서 Aside로 공개 페이지 한 곳을 읽고 제목·주소·내용을 알려줘.'
  },
  connect: {
    next: '오류 전체와 어느 단계에서 발생했는지 확인하세요. fetch failed·EACCES·인증 실패는 같은 원인이라고 단정할 수 없습니다. 실행 계정·로컬 연결과 이미 허용된 경로부터 확인합니다.',
    anchor: 'aside-auth',
    prompt: 'Aside 인증 또는 연결 오류가 났어. 아래 원문과 발생 단계를 확인해줘.\n브라우저 실행·CLI 계정 확인·Codex의 실행 계정·로컬 서비스 접근을 나눠 점검해줘.\n같은 OS 사용자라는 말은 이메일이 아니라 명령을 실행하는 컴퓨터 계정인지 확인해줘.\n보안 끄기·관리자 실행·인증 키 삭제·반복 재설치부터 하지 마.\n허용된 경로로 실제 페이지를 읽고, 막힌 단계와 사람이 해야 할 한 가지를 구분해줘.'
  },
  git: {
    next: '폴더는 실제 파일, Git은 변경 기록, GitHub는 원격 보관입니다. 기존 폴더와 저장소부터 확인하고, 미커밋 변경·분기·충돌은 보존합니다.',
    anchor: 'git',
    prompt: '지금 실습 폴더에서 Git 사용 상태·원격·현재 브랜치·변경 파일부터 확인해줘.\n이미 있는 폴더와 저장소를 재사용하고 중복 클론하지 마.\n깨끗할 때만 fetch 후 프로젝트 기준 브랜치로 ff-only 최신화를 진행해줘.\n미커밋 변경·분기·충돌이 있으면 보존하고 선택이 필요한 부분을 알려줘.\n본인 비공개 저장소를 쓸 수 있게 안내하고 비밀번호·개인정보는 올리지 마.\n작업 규칙과 완료 기록을 파일에 남기고 커밋·푸시·배포를 각각 구분해줘.'
  }
};
function updateSelfCheck() {
  const choice = selfCheckCases[document.getElementById('check-symptom').value];
  const answer = document.getElementById('check-answer');
  answer.hidden = !choice;
  if (!choice) return;
  document.getElementById('check-next').textContent = choice.next;
  document.getElementById('check-prompt').textContent = '내 컴퓨터: ' + document.getElementById('check-os').value + '\n' + choice.prompt + '\n\n막힌 단계:\n오류 문구(비밀번호·토큰·개인정보는 가리고):\n이미 해 본 것과 결과:';
  document.getElementById('check-more').href = '#' + choice.anchor;
  answer.querySelector('.copy-status').textContent = '';
}
for (const id of ['check-os', 'check-symptom']) document.getElementById(id).addEventListener('change', updateSelfCheck);
