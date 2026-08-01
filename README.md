<div align="center">
  <img src="assets/mark.svg" width="112" alt="Apple HIG Design Studio mark">
  <h1>Apple HIG Design Studio</h1>
  <p>An evidence-first Codex skill for designing, implementing, reviewing, and auditing Apple-platform interfaces.</p>

  [![Validate](https://github.com/Sunwood-ai-labs/design-with-apple-hig/actions/workflows/validate.yml/badge.svg)](https://github.com/Sunwood-ai-labs/design-with-apple-hig/actions/workflows/validate.yml)
  [![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)

  [日本語](README.ja.md)
</div>

## ✨ Overview

`design-with-apple-hig` coordinates current Apple primary guidance, framework facts, accessibility evidence, rendered observations, specialist heuristics, and static audit signals without treating them as equally authoritative.

It supports:

- iOS, iPadOS, macOS, watchOS, tvOS, and visionOS
- SwiftUI, UIKit, and AppKit implementation work
- design, build, review, scoring, refactoring, and audit workflows
- Dynamic Type, VoiceOver, semantic colors, adaptive layouts, Reduce Motion, and representative UI states
- Apple-inspired Web and cross-platform work while preserving host-platform conventions

## 🧭 Why this skill exists

Many community HIG skills mix official requirements, old snapshots, personal heuristics, fixed numbers, and cross-platform generalizations. This skill uses a stricter model:

1. Current Apple HIG and official design resources arbitrate Apple design claims.
2. Current SDK documentation arbitrates API and framework behavior.
3. Accessibility standards and platform features support accessibility claims.
4. Third-party skills are narrow specialists, not authorities.
5. Static audit results are evidence to inspect, not proof of HIG compliance.

## 🚀 Install

Clone the repository into your Codex skills directory:

```powershell
git clone https://github.com/Sunwood-ai-labs/design-with-apple-hig.git "$env:USERPROFILE\.codex\skills\design-with-apple-hig"
```

Restart or refresh Codex so the skill list is reloaded.

## 💬 Use

Invoke the skill explicitly:

```text
Use $design-with-apple-hig to review and refactor this SwiftUI screen.
```

For an evidence-separated review:

```text
Use $design-with-apple-hig to review this interface. Separate Apple guidance,
framework facts, accessibility evidence, visible observations, audit signals,
and heuristics. Score only verified dimensions.
```

## 🏗️ Architecture

```text
SKILL.md
├── classify task, platform, framework, artifact, and input model
├── retrieve the smallest current primary-source bundle
├── preserve source scope and wording strength
├── route only relevant specialist capabilities
└── verify implementation, rendering, accessibility, and findings

references/
├── official-source-map.md   Apple primary-source routing
├── source-routing.md        authority and conflict resolution
├── platform-routing.md      Apple-native, Web, and cross-platform boundaries
├── review-rubric.md         evidence-based severity and scoring
├── verification-loop.md     build, render, interaction, and re-test loop
└── bibliography.md          audited sources and incorporation policy
```

## 🔎 Evidence model

Material recommendations are separated into these classes:

| Evidence | Meaning |
| --- | --- |
| `APPLE` | Confirmed in current Apple primary guidance |
| `FRAMEWORK` | Confirmed by current SDK or framework behavior |
| `ACCESSIBILITY` | Supported by an applicable accessibility standard or feature |
| `OBSERVATION` | Visible in supplied code, screenshots, prototypes, or a running UI |
| `AUDIT` | Reported by a static analyzer and still requiring contextual review |
| `HEURISTIC` | A reasoned design recommendation, not an Apple requirement |

## ✅ Validate

Run the repository checks locally:

```powershell
uv run scripts/validate_repository.py
```

Read a current official HIG topic through Apple's DocC JSON fallback:

```powershell
uv run scripts/fetch_apple_hig.py materials --metadata-only
```

GitHub Actions runs the structural validator and Python compilation checks on every push and pull request.

## 📚 Sources and provenance

The skill includes an audited [bibliography](references/bibliography.md) covering Apple primary sources and the community skills or tools that informed limited specialist roles. Third-party HIG corpora and Apple documentation are linked rather than copied.

See the [official source map](references/official-source-map.md) for runtime routing. Exact values, current APIs, OS-specific behavior, and normative claims must be rechecked against current Apple sources when the skill runs.

## ⚖️ License

Original project code and documentation are available under the [MIT License](LICENSE). Linked Apple materials, trademarks, design resources, and third-party projects remain subject to their respective terms and licenses.

## ℹ️ Disclaimer

This is an independent community project. It is not affiliated with, endorsed by, or sponsored by Apple Inc. “Apple,” platform names, and related marks are trademarks of Apple Inc. A review produced by this skill is evidence-backed guidance, not an Apple certification.
