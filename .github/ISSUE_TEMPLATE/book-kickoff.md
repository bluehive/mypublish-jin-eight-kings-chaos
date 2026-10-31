---
name: 書籍キックオフ
about: 次冊の執筆開始 — 正本・フォーマット・章Issue一覧を決める
title: "[企画] "
labels: ''
assignees: ''
---

## 書籍情報

- **タイトル**:
- **スラッグ**（フォルダ名）: `<!-- 例: jin-eight-kings-chaos -->`
- **副題**:
- **目標語数**:

## 配布フォーマット方針（先に固定）

> **次冊以降のデフォルト出力は EPUB（横書き）** です。

- [ ] **必須**: 横書き EPUB（`build.py --format epub-horizontal --no-cover`）
- [ ] 縦書き EPUB（必要時にビルド機能を追加）
- [ ] DOCX（必要時にビルド機能を追加）
- **表紙**: なし（表紙付き出力は必要時に実装）
- **目次**: あり（EPUB ビルド時に自動生成）

## ディレクトリ準備

- [ ] `manuscript/<slug>/book.md` — **生成原稿**（直接編集せず、章ドラフトから結合）
- [ ] `drafts/<slug>/` — 章ドラフト
- [ ] `notes/<slug>/` — 用語集・data-pack
- [ ] `scripts/<slug>/` — `combine_drafts.py` + `build.py`
- [ ] `output/<slug>/` — 配布物

## 章 Issue 一覧

| 章 | Issue | 状態 |
|----|-------|------|
| 序章 | # | OPEN |
| 第1章 | # | |
| … | | |

## 標準ビルドコマンド（Issue に必ず1行で書く）

```bash
python3 scripts/<slug>/build.py --format epub-horizontal --no-cover --verify
```

## 関連

- 企画リポジトリ:
- 前冊との連続性:

## メモ

<!-- Issue #15 提案B/F 実装テンプレ / 2026-06-20 -->
