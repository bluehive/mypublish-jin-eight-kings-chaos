# 移行記録

- 移行準備日: 2026-10-31（日本時間）
- 状態: PR でユーザー承認待ち。移行元の原稿は承認まで維持。
- 移行元: `bluehive/draft-publish-books-2026`
- 元コミット: `4c85e02d7f8eadad93bca3dd00537457a2d53715`
- 元パス: `jin-eight-kings-chaos.md`
- 保存先: `notes/jin-eight-kings-chaos/outline.md`（バイト単位で原文保存）
- 原文 SHA-256: `15cf2fd2009fba33dd980aba4775a1a2bb4b54125fc15f61a8adbb49bf05d038`
- 構成参考: `bluehive/mypublish-japanism` の `33b48e78099cb5d58bd8919f6845857efb4a9601`

参考リポジトリのフォルダ構成・章ドラフトから結合原稿を生成する方式・横書き EPUB 方針・Issue テンプレートを採用しました。CSS は参考元から引き継ぎ、ビルドスクリプトは本書用の最小構成で用意しています。参考書籍の本文や調査資料は含めません。

`outline.md` は企画段階の記録です。「関連書籍（本リポジトリ内）」は移行元を指します。関連企画『竹林七賢』の所在は [notes README](README.md) を参照してください。

元原稿の史実・章数表現・付録の重複項番・旧出版目標は未修正で保存しています。章ドラフトも構成のみを引き継ぎ、本文や新しい出版日を補っていません。正本の Git 履歴はこの移行コミットから始まります。以前の履歴は移行元リポジトリで確認できます。

## 承認後の移行元整理

[source-cleanup.patch](source-cleanup.patch) に、移行元 README の移行案内・一覧更新と旧原稿の削除をまとめています。
PR マージ後に公開先の原文が一致することを再確認し、移行元でパッチを適用します。承認待ちの間は適用しません。

```bash
git apply --check /path/to/source-cleanup.patch
git apply /path/to/source-cleanup.patch
```

実行先は `draft-publish-books-2026` の最新チェックアウトです。パッチの適用確認で競合した場合は最新 README に合わせて調整します。
