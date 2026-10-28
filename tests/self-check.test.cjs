const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '../3기/실습');
const html = fs.readFileSync(path.join(root, '3기_4주차_실습하다_막혔을때_해결안내.html'), 'utf8');
const script = fs.readFileSync(path.join(root, '실습_자가진단.js'), 'utf8');

test('all symptom and OS choices are real option elements', () => {
  for (const [id, expected] of [['check-os', ['모르겠음', 'Windows', 'Mac']], ['check-symptom', ['', 'chat', 'computer', 'cli', 'connect', 'git']]]) {
    const select = html.match(new RegExp('<select id="' + id + '">([\\s\\S]*?)</select>'));
    assert.ok(select);
    const options = [...select[1].matchAll(/<option value="([^"]*)">[^<]*<\/option>/g)].map(m => m[1]);
    assert.deepEqual(options, expected);
  }
});

test('every choice supplies a prompt and an existing help destination', () => {
  const nodes = Object.fromEntries(['check-os', 'check-symptom', 'check-answer', 'check-next', 'check-prompt', 'check-more'].map(id => [id, {value:'', textContent:'', hidden:true, addEventListener(){}, querySelector(){return {textContent:''};}}]));
  const context = vm.createContext({document:{getElementById:id=>nodes[id]}});
  vm.runInContext(script, context);
  const prompts = new Set();
  for (const os of ['모르겠음', 'Windows', 'Mac']) {
    for (const symptom of ['chat','computer','cli','connect','git']) {
      nodes['check-os'].value=os;nodes['check-symptom'].value=symptom;
      vm.runInContext('updateSelfCheck()', context);
      assert.equal(nodes['check-answer'].hidden, false);
      assert.ok(nodes['check-prompt'].textContent.startsWith('내 컴퓨터: '+os));
      assert.match(nodes['check-prompt'].textContent, /이미 해 본 것과 결과:/);
      assert.ok(html.includes('id="'+nodes['check-more'].href.slice(1)+'"'));
      prompts.add(nodes['check-prompt'].textContent);
    }
  }
  assert.equal(prompts.size,15);
  nodes['check-symptom'].value='';vm.runInContext('updateSelfCheck()',context);
  assert.equal(nodes['check-answer'].hidden,true);
});
