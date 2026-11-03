#!/usr/bin/env python3
"""Combine chapter sources; --check fails when the generated manuscript is stale."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'jin-eight-kings-chaos'
DRAFTS = ROOT / 'drafts' / SLUG
BOOK = ROOT / 'manuscript' / SLUG / 'book.md'
CHAPTER_FILES = (
    ['ch01-preface-draft.md']
    + [f'ch{i:02d}-draft.md' for i in range(2, 9)]
    + ['ch99-epilogue-draft.md', 'ch98-appendices-draft.md']
)


def combine_text():
    front = '''---
title: "晋・八王の乱と混沌——司馬氏天下の崩壊"
subtitle: "西晋の短期統一と内乱が中国中世を開いた"
lang: ja
---

> 全体初稿・本文分量80％: 序章〜第7章・終章の全43節を執筆。本文64,049字（8万字基準80.0％）。付録・図版は未作成です。
> 本文は史料・研究史の追加校訂を要します。進捗の算定は notes/jin-eight-kings-chaos/progress.md を参照。
> 副題は案、著者・出版日は未設定です。
'''
    return '\n\n'.join([front.rstrip()] + [
        (DRAFTS / name).read_text(encoding='utf-8').rstrip('\n')
        for name in CHAPTER_FILES
    ]) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    content = combine_text()
    if args.check:
        if not BOOK.exists() or BOOK.read_text(encoding='utf-8') != content:
            raise SystemExit('FAIL: book.md が未生成または古いため、再結合してください。')
        print('PASS: draft → book.md')
    else:
        BOOK.parent.mkdir(parents=True, exist_ok=True)
        BOOK.write_text(content, encoding='utf-8')
        print(f'Generated {BOOK.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
