# mypublish-jin-eight-kings-chaos

**『晋・八王の乱と混沌——司馬氏天下の崩壊』** の企画・執筆用公開リポジトリです。
副題案: 西晋の短期統一と内乱が中国中世を開いた。

`mypublish-japanism` の章ドラフト → 結合原稿 → 横書き EPUB の構成を参考にしています。
現在は目次段階で、本文は未執筆です。想定分量は8万〜12万字。原案の出版目標（2026年9月11日）は経過しており、出版日は再設定が必要です。

## 企画と編集元

- [企画・目次の正本](notes/jin-eight-kings-chaos/outline.md) — 移行元の原文を保存
- [企画メモ](drafts/jin-eight-kings-chaos/ch00-concept-draft.md)
- [調査メモ](notes/jin-eight-kings-chaos/README.md)
- [移行記録](notes/jin-eight-kings-chaos/MIGRATION.md)

```text
drafts/jin-eight-kings-chaos/       # 編集元（序章・第1〜7章・終章・付録）
manuscript/jin-eight-kings-chaos/   # 章ドラフトから生成する book.md
notes/jin-eight-kings-chaos/        # 企画・目次・史料・移行記録
scripts/jin-eight-kings-chaos/      # 結合・ビルド・鮮度確認
output/jin-eight-kings-chaos/       # EPUB の出力先
assets/epub/                      # 横書き CSS
images/                           # 表紙・地図・系譜図（今後作成）
.github/ISSUE_TEMPLATE/            # 企画・章・一般タスク
```

本文は `drafts/jin-eight-kings-chaos/` で編集します。`ch00-concept-draft.md` は結合対象外です。
`book.md` は生成物なので直接編集せず、ドラフト更新後に再生成します。
原案の節見出しを章ごとのひな形に展開していますが、本文・史実・表記の校訂はこれからです。

## 結合とビルド

必要環境: Python 3.10以上。EPUB 出力には PATH 上の Pandoc 3以上が必要です。
Python の追加ライブラリは不要です。

```bash
python3 scripts/jin-eight-kings-chaos/combine_drafts.py
python3 scripts/jin-eight-kings-chaos/combine_drafts.py --check
python3 scripts/jin-eight-kings-chaos/build.py --format epub-horizontal --no-cover --verify
```

ビルドは原稿を再結合し、目次付き横書き EPUB を作ります。`--verify` で原稿の鮮度、EPUB の ZIP・XML・目次を確認し、失敗時は終了コードを返します。
現段階の生成原稿・EPUB には「本文未執筆」の表示が入り、内容の正確性や出版品質を保証する検証は行いません。
著者名・新しい出版日・表紙は未設定です。縦書き・DOCX は必要時に追加します。

## 執筆の進め方

1. 企画の章構成を確認し、章 Issue で史料・到達目標を整理する。
2. 調査根拠を `notes/`、本文を `drafts/` に記録する。
3. 結合・ビルド後に内容と表示を確認する。
4. 完成時に配布物を `output/` で管理する。

関連企画『竹林七賢』は [移行元](https://github.com/bluehive/draft-publish-books-2026/blob/main/seven-sages-bamboo-grove.md) にあります。
