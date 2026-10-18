#!/usr/bin/env python3
"""Render the Markdown originals as static GitHub Pages documents."""

from __future__ import annotations

import html
import re
import unicodedata
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [ROOT / "README.md", *sorted(ROOT.glob("[0-9][0-9]-*.md"))]
DESCRIPTIONS = {
    "README": "E3에서 E7까지, 책임의 범위로 살펴보는 AI 시대의 개발자 성장 가이드.",
    "01-level-map": "직급이 오르면서 달라지는 문제·자율성·기술 판단·영향 범위.",
    "02-self-assessment": "최근 작업의 증거로 지금의 강점과 다음 책임을 찾는 자기 진단.",
    "03-e3-junior": "작은 기능을 만들고, 확인하고, 설명하는 Junior의 책임.",
    "04-e4-mid-level": "요구사항부터 출시·운영·복구까지 프로젝트를 완수하는 책임.",
    "05-e5-senior": "다음 문제를 정하고 동료와 함께 팀의 성과를 만드는 책임.",
    "06-e6-staff": "다른 숙련자들과 경계를 넘는 병목을 해결하는 Staff의 책임.",
    "07-e7-senior-staff": "불분명한 기회를 발견하고 중요한 사업 결과로 연결하는 책임.",
    "08-principal-and-paths": "Principal 이후, 기술 리더·매니저·창업의 책임과 선택.",
    "09-ai-collaboration": "레벨별 AI 위임·검증·학습·권한과 관련 연구의 한계.",
    "10-technical-foundations": "만들면서 원리를 배우는 레벨별 기술 학습 지도.",
    "11-entrepreneur-path": "기능 제작에서 고객 가치·운영·사업 판단으로 넓어지는 책임.",
    "12-growth-plan": "다음 책임을 연습하고 증거를 남기는 2주·6주·12주 계획.",
    "13-templates": "자기 진단, AI 요청, 기술 결정, 성과, 피드백을 위한 복사 양식.",
    "14-video-notes": "참고 영상의 타임스탬프와 로드맵으로 재구성한 성장 원칙.",
    "15-sources": "기업의 공개 경력 체계, AI 연구, 공식 학습 자료와 해석의 한계.",
}


def output_name(path: Path) -> str:
    return "index.html" if path.stem == "README" else path.with_suffix(".html").name


def title_of(path: Path) -> str:
    return path.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")


def slugify(value: str, separator: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[\s_-]+", separator, value).strip(separator)


def rewrite_link(match: re.Match[str]) -> str:
    target = match.group(1)
    if re.match(r"(?:https?:|mailto:|#)", target):
        return match.group(0)
    path, sep, fragment = target.partition("#")
    if path.endswith(".md"):
        path = "index.html" if path == "README.md" else path[:-3] + ".html"
    return f'href="{path}{sep}{fragment}"'


def navigation(current: Path) -> str:
    links = []
    for path in CHAPTERS:
        label = "처음으로 · 읽기 안내" if path.stem == "README" else title_of(path)
        active = ' aria-current="page"' if path == current else ""
        links.append(
            f'<a href="{output_name(path)}"{active}>{html.escape(label)}</a>'
        )
    return "\n".join(links)


def render(path: Path, position: int) -> None:
    source = path.read_text(encoding="utf-8")
    title = title_of(path)
    converter = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"slugify": slugify, "toc_depth": "2-3"}},
        output_format="html5",
    )
    body = converter.convert(source)
    body = re.sub(r'href="([^"]+)"', rewrite_link, body)
    body = re.sub(r"<table>(.*?)</table>", r'<div class="table-scroll" tabindex="0" role="region" aria-label="가로로 스크롤할 수 있는 표"><table>\1</table></div>', body, flags=re.S)
    is_home = path.stem == "README"
    hero = ""
    if is_home:
        body = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)
        hero = '''<section class="hero" aria-labelledby="hero-title">
<p class="eyebrow">A FIELD GUIDE FOR YOUR NEXT LEVEL</p>
<h1 id="hero-title">AI 시대 개발자<br>성장 로드맵</h1>
<p class="hero-copy">지금의 위치를 증거로 돌아보고,<br>다음 레벨에서 맡을 책임을 찾습니다.</p>
<div class="hero-actions"><a class="button" href="02-self-assessment.html">내 위치 점검하기 <span aria-hidden="true">↗</span></a><a href="01-level-map.html">레벨 지도 먼저 읽기 →</a></div>
<ol class="level-strip" aria-label="중심이 되는 다섯 레벨">
<li><a href="03-e3-junior.html"><b>E3</b><span>Junior</span><small>작은 기능</small></a></li>
<li><a href="04-e4-mid-level.html"><b>E4</b><span>Mid-level</span><small>프로젝트</small></a></li>
<li><a href="05-e5-senior.html"><b>E5</b><span>Senior</span><small>팀의 방향</small></a></li>
<li><a href="06-e6-staff.html"><b>E6</b><span>Staff</span><small>경계를 넘는 성과</small></a></li>
<li><a href="07-e7-senior-staff.html"><b>E7</b><span>Senior Staff</span><small>사업의 기회</small></a></li>
</ol><p class="hero-note">영상의 E3~E7을 바탕으로 재구성한 학습 가이드 · 기업의 공식 승진 규정과 구분합니다.</p>
</section>'''
    pager = []
    if position > 0:
        previous = CHAPTERS[position - 1]
        pager.append(f'<a href="{output_name(previous)}"><small>이전 문서</small>{html.escape(title_of(previous))}</a>')
    if position + 1 < len(CHAPTERS):
        following = CHAPTERS[position + 1]
        pager.append(f'<a href="{output_name(following)}"><small>다음 문서</small>{html.escape(title_of(following))} →</a>')
    canonical = f"https://aiautomationstudy.github.io/study_exercises/ai-developer-roadmap/{output_name(path)}"
    page_title = title if is_home else f"{title} | AI 시대 개발자 성장 로드맵"
    page = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(DESCRIPTIONS[path.stem], quote=True)}">
<meta name="theme-color" content="#123e3b"><link rel="canonical" href="{canonical}">
<link rel="icon" href="data:,"><link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script>
</head><body class="{'home' if is_home else 'chapter'}">
<a class="skip-link" href="#main">본문으로 바로 가기</a>
<header class="site-header"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">↗</span><span>AI 시대 개발자 <b>성장 로드맵</b></span></a><span class="edition">2026.10 · 16편의 가이드</span></header>
<div class="layout"><aside class="sidebar"><details id="chapter-menu" open><summary>전체 문서 <span aria-hidden="true">⌄</span></summary>
<label class="search-label" for="chapter-search">문서 제목 검색</label><input id="chapter-search" type="search" placeholder="레벨, AI, 창업…" autocomplete="off">
<nav id="chapter-nav" aria-label="전체 문서">{navigation(path)}</nav><p id="search-status" class="search-status" role="status"></p>
</details><p class="sidebar-note">작게 만들고, 끝까지 확인하고,<br>책임의 범위를 넓혀 갑니다.</p></aside>
<main id="main" tabindex="-1"><div class="reading-meta"><span>{'START HERE · 읽기 안내' if is_home else f'GUIDE {position:02d} / 15'}</span><a class="source-link" href="{path.name}" download>Markdown 원문 ↓</a></div>
{hero}<article class="prose">{body}</article>
<nav class="pager" aria-label="이전·다음 문서">{''.join(pager)}</nav>
<footer>기준일 2026.10.18 · 학습과 성장 대화를 위한 자료<br><a href="15-sources.html">출처와 해석의 한계</a> · <a href="README.md">읽기 안내 원문</a> · <a href="#main">맨 위로 ↑</a></footer>
</main><aside class="toc-panel"><p class="eyebrow">이 문서의 목차</p><nav aria-label="현재 문서 목차">{converter.toc}</nav><a class="toc-start" href="02-self-assessment.html">오늘의 첫 행동<br><b>최근 작업 3개로 점검하기 →</b></a></aside></div>
<div id="copy-status" class="copy-status" role="status" aria-live="polite"></div>
</body></html>'''
    (ROOT / output_name(path)).write_text(page, encoding="utf-8")


if __name__ == "__main__":
    for index, chapter in enumerate(CHAPTERS):
        render(chapter, index)
    print(f"Rendered {len(CHAPTERS)} Markdown originals as static HTML pages.")
