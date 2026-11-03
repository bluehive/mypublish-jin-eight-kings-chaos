# 執筆進捗（全体初稿）

更新日：2026-11-03（JST）

## 到達点と80％の意味

序章〜第7章・終章の全43節に本文がある。本文64,049字、企画下限8万字の80.0％。前半39,941字から24,108字を追加した。第5章の全5節を含み、長安・東晋成立・人物論・終章まで通読できる全体初稿である。付録は企画項目のみで、本文字数にも節数にも含めない。

**80％は初稿本文の分量の目安であり、出版品質の完成率ではない。** 10万字基準で64.0％、12万字基準で53.4％。全43節に本文があることも、史料校訂完了を意味しない。最終稿では約1万6千字を機械的に追加するのでなく、研究史・地域事例・付録を補い、重複を削って分量を再評価する。

## 字数と再現方法

Unicode文字数。空白・改行、見出し、初稿表示、表、HTMLコメント、章末の「史料と確認範囲」を除く。句読点は含み、生成したbook.mdを重複計上しない。本文中のMarkdown強調等がある場合は記号も文字として数える（前半の算定と同じ文字列方式）。

| 編集元 | 本文字数 |
|---|---:|
| `ch01-preface-draft.md` | 5,237 |
| `ch02-draft.md` | 8,565 |
| `ch03-draft.md` | 9,466 |
| `ch04-draft.md` | 7,228 |
| `ch05-draft.md` | 9,461 |
| `ch06-draft.md` | 8,770 |
| `ch07-draft.md` | 8,850 |
| `ch08-draft.md` | 4,890 |
| `ch99-epilogue-draft.md` | 1,582 |
| **合計** | **64,049** |


リポジトリルートでの再計算：

```python
from pathlib import Path
import re
files = (['ch01-preface-draft.md']
         + [f'ch{i:02d}-draft.md' for i in range(2, 9)]
         + ['ch99-epilogue-draft.md'])
total = 0
for name in files:
    text = (Path('drafts/jin-eight-kings-chaos') / name).read_text()
    text = text.split('\n### ')[0]
    body = ''.join(line for line in text.splitlines()
                   if line and not line.startswith(('#', '>', '|', '<!--')))
    count = len(re.sub(r'\s', '', body))
    print(name, count)
    total += count
print('total', total)
print('8万字比', round(total / 800, 1))
```

## 追加した根拠と範囲

- 第5章：[データパック](data-packs/ch06_data_pack.md)。李特載記、李矩伝、劉元海載記、懐帝紀の具体例。
- 第6章：[データパック](data-packs/ch07_data_pack.md)。愍帝紀・元帝紀、王導・王敦・祖逖伝、通鑑89。
- 第7章：前半で扱った人物の史料批判と、阮籍伝の追加。終章は本文の総合。
- 所在と留保：[全体初稿照合記録](factcheck/whole-draft-2026-11-03.md)、[sources.md](sources.md)、各章末。
- 編集元だけを編集し、結合原稿はスクリプトから生成。原案outline.mdは移行原文のまま保存。

## 残る約20％の作業

- 全巻の版本・訳書と頁、異同、研究史。前半の[照合ノート](factcheck/first-half-draft-2026-11-01.md)の保留も継続。
- 第5〜6章の地域差・人口・土地・官制を二次研究で補強。本文の一般論と留保を整理する。
- 第7章の前半との重複削減、書簡・著作・人物研究の追加。終章を全巻校訂後に推敲。
- 付録の年表、系譜、戦役、地名、参考文献、地図。報告書未確認の出土史料は使わない。
- 著者名、出版日、表紙、端末表示、出版用検証。

## PRとIssue

PR #6の承認済みhead `1e31bab6ed292727fcf4fedfb3efe2dc5515b4a3`を継承する。今回のPRはそのブランチをbaseにして追加分をレビューできるようにする。マージは今回のユーザー承認後。

Issue #3は版本・訳書等の課題が残るため維持。Issue #7は今回のPRで対応し、マージ前は開いたままにする。不要・重複として即時閉鎖するIssueはなかった。

## 検証

- `combine_drafts.py --check`：PASS。
- `build.py --format epub-horizontal --no-cover --verify`：PASS。鮮度・ZIP・XML・目次を確認。
- `git diff --check`：PASS。
- 全43節の本文、未執筆コメントの除去、追加分の相対リンク、EPUB内の章・節と80％表示を点検。
- Pandocは日本語翻訳データとAbstractの訳語に警告。EPUBの生成・構造検証は成功。端末表示と史実校訂は未完。
