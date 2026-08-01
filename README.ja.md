<div align="center">
  <img src="assets/mark.svg" width="112" alt="Apple HIG Design Skill マーク">
  <h1>Apple HIG Design Skill</h1>
  <p><code>design-with-apple-hig</code></p>
  <p>Appleプラットフォームの設計・実装・レビュー・監査を、一次情報から進めるCodexスキルです。</p>

  [![Validate](https://github.com/Sunwood-ai-labs/design-with-apple-hig/actions/workflows/validate.yml/badge.svg)](https://github.com/Sunwood-ai-labs/design-with-apple-hig/actions/workflows/validate.yml)
  [![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)

  [English](README.md)
</div>

## ✨ 概要

`design-with-apple-hig` は、最新のApple公式ガイダンス、SDKの事実、アクセシビリティ根拠、画面上の観察、専門スキルのヒューリスティック、静的監査の検出結果を、権威の異なる証拠として整理して扱います。

主な対象は次のとおりです。

- iOS、iPadOS、macOS、watchOS、tvOS、visionOS
- SwiftUI、UIKit、AppKitによる実装
- 設計、実装、レビュー、採点、リファクタリング、監査
- Dynamic Type、VoiceOver、semantic color、適応レイアウト、Reduce Motion、代表状態の検証
- ホスト側の規範を守ったApple-inspired WebおよびクロスプラットフォームUI

## 🧭 このスキルが必要な理由

コミュニティ製HIGスキルには、公式要件、古いスナップショット、個人的なヒューリスティック、固定数値、プラットフォームをまたぐ一般化が混在する場合があります。本スキルは次の優先順位を守ります。

1. Appleのデザイン判断は、最新のApple HIGと公式Design Resourcesで裁定する。
2. APIと実装挙動は、現行SDKドキュメントで裁定する。
3. アクセシビリティ上の主張は、適用可能な標準とプラットフォーム機能で裏付ける。
4. 第三者スキルは限定的な専門家として使い、規範の裁定者にはしない。
5. 静的監査結果を、HIG準拠の証明として扱わない。

## 🚀 インストール

Codexのskillsディレクトリへcloneします。

```powershell
git clone https://github.com/Sunwood-ai-labs/design-with-apple-hig.git "$env:USERPROFILE\.codex\skills\design-with-apple-hig"
```

Codexを再起動または更新し、スキル一覧を再読み込みしてください。

## 💬 使い方

スキルを明示的に呼び出します。

```text
Use $design-with-apple-hig to review and refactor this SwiftUI screen.
```

証拠の種類を分離してレビューする例です。

```text
Use $design-with-apple-hig to review this interface. Separate Apple guidance,
framework facts, accessibility evidence, visible observations, audit signals,
and heuristics. Score only verified dimensions.
```

## 🏗️ 構成

```text
SKILL.md
├── タスク、PF、Framework、成果物、入力方式を分類
├── 必要最小限の最新一次資料を取得
├── 原典の適用範囲と表現強度を維持
├── 関係する専門機能だけをルーティング
└── 実装、描画、アクセシビリティ、findingを再検証

references/
├── official-source-map.md   Apple一次資料へのルーティング
├── source-routing.md        権威順位と競合解決
├── platform-routing.md      Apple-native、Web、cross-platformの境界
├── review-rubric.md         証拠ベースの重大度と採点
├── verification-loop.md     build、描画、操作、再テスト
└── bibliography.md          精査した資料と採用方針
```

## 🔎 証拠モデル

重要な推奨を次のクラスへ分離します。

| Evidence | 意味 |
| --- | --- |
| `APPLE` | 現在のApple一次資料で確認済み |
| `FRAMEWORK` | 現行SDKまたはFrameworkの挙動で確認済み |
| `ACCESSIBILITY` | 適用可能なアクセシビリティ標準または機能で裏付け済み |
| `OBSERVATION` | コード、スクリーンショット、プロトタイプ、実動UIから観察可能 |
| `AUDIT` | 静的解析の検出結果。文脈確認が必要 |
| `HEURISTIC` | 妥当な設計提案だがApple公式要件ではない |

## ✅ 検証

ローカルでリポジトリ検証を実行します。

```powershell
uv run scripts/validate_repository.py
```

Apple公式DocC JSONから、現在のHIGトピックを確認できます。

```powershell
uv run scripts/fetch_apple_hig.py materials --metadata-only
```

GitHub Actionsでも、pushとpull requestごとに構造検証とPythonコンパイル検査を実行します。

## 📚 参考文献と出典管理

[参考文献](references/bibliography.md)には、Apple一次資料と、限定的な専門ロールの参考にしたコミュニティスキル・ツールを記録しています。第三者のHIGコーパスやApple文書本文は複製せず、参照先と採用判断だけを保持します。

実行時の参照先は[公式資料マップ](references/official-source-map.md)を確認してください。正確な数値、現行API、OS固有の挙動、規範的な主張は、スキル実行時に最新のApple公式資料で再確認します。

## ⚖️ ライセンス

本プロジェクト独自のコードと文書は[MIT License](LICENSE)で公開します。リンク先のApple資料、商標、Design Resources、第三者プロジェクトには、それぞれの利用条件とライセンスが適用されます。

## ℹ️ 免責事項

本プロジェクトは独立したコミュニティプロジェクトであり、Apple Inc.との提携、承認、支援関係はありません。「Apple」および各プラットフォーム名等はApple Inc.の商標です。本スキルによるレビューは証拠に基づく設計支援であり、Appleによる認証ではありません。
