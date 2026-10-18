"use strict";

const search = document.getElementById("chapter-search");
const chapterLinks = [...document.querySelectorAll("#chapter-nav a")];
search.addEventListener("input", () => {
  const query = search.value.trim().toLocaleLowerCase("ko");
  let found = 0;
  chapterLinks.forEach((link) => {
    link.hidden = !link.textContent.toLocaleLowerCase("ko").includes(query);
    if (!link.hidden) found += 1;
  });
  document.getElementById("search-status").textContent = query ? `${found}개 문서` : "";
});

const chapterMenu = document.getElementById("chapter-menu");
if (window.matchMedia("(max-width: 800px)").matches) chapterMenu.open = false;

document.querySelectorAll(".prose pre").forEach((block) => {
  const code = block.querySelector("code");
  if (!code) return;
  const button = document.createElement("button");
  button.className = "copy-button";
  button.type = "button";
  button.textContent = "양식 복사";
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(code.textContent);
      document.getElementById("copy-status").textContent = "복사했습니다.";
      button.textContent = "복사 완료";
      setTimeout(() => {
        button.textContent = "양식 복사";
        document.getElementById("copy-status").textContent = "";
      }, 2200);
    } catch {
      document.getElementById("copy-status").textContent = "자동 복사를 사용할 수 없습니다. 양식의 글을 선택해 복사해 주세요.";
    }
  });
  block.appendChild(button);
});
