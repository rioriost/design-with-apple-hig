# Verification loop

Use this file after implementation or when reviewing a runnable artifact. Match effort to risk and report omitted checks with their confidence impact.

## 1. Establish baseline and evidence

- Record platform, OS and SDK range, framework, build configuration, representative device/window, input, appearance, data, and state.
- Preserve pre-existing failures and unrelated user changes.
- Capture equivalent pre-change rendering or behavior when comparison matters.
- Retrieve current HIG pages for disputed or exact claims. Record URLs and dates.
- Run static audit before edits when available and relevant; keep raw versioned output.

When Apple HTML extraction fails, use:

```bash
python scripts/fetch_apple_hig.py <topic-slug> --metadata-only
python scripts/fetch_apple_hig.py <topic-slug>
```

Do not save the fetched page as a bundled corpus.

## 2. Run repository-native checks

Use existing formatter, linter, type checker, unit tests, UI/snapshot tests, and target-platform build. Prefer project-pinned commands and versions. Inspect existing CI and project instructions before inventing commands.

If a command cannot run, report the command, concise reason, and affected coverage. Compilation establishes buildability, not design quality.

## 3. Render representative states

Select risk-based states from the platform matrix:

- Compact/regular or minimum/normal/maximum window
- Light/Dark, normal/increased contrast, reduced transparency where applicable
- Default and large accessibility text; long localization and RTL if relevant
- Standard and Reduced Motion
- Loading, populated, empty, error, offline, and partial success
- Focused, selected, disabled, pressed, validation, and destructive states

Inspect hierarchy, clipping, overlap, unintended scrolling, safe areas, target separation, focus visibility, material contrast, density, and state continuity. A screenshot-only input leaves runtime dimensions unverified.

## 4. Test interaction and accessibility

Verify as applicable:

- Semantic role, accessible name, value, state, actions, hints, and announcements
- Focus and reading order
- Completion using keyboard, remote, pointer, Crown, eyes/hands, touch, voice, or switch alternatives
- Text scaling without loss of content or action
- Contrast and non-color state cues
- Reduce Motion, Reduce Transparency, Increase Contrast, Bold Text, and Differentiate Without Color behavior supported by the platform
- Validation, progress, cancel, interruption, error recovery, and partial failure
- Destructive confirmation, undo, or recovery
- Permission requests in a context that explains value without coercion

Use Accessibility Inspector and real assistive technology when available. Do not infer VoiceOver behavior from modifiers or labels alone.

## 5. Use HIG Doctor as a bounded analyzer

Prefer the project-pinned package. Otherwise, when network execution is authorized and useful:

```bash
npx -y hig-doctor <project-or-file> --stdout
```

At the 2026-08-01 audit baseline, HIG Doctor advertised 431 rules but its bundled HIG content was a frozen 2025-02-02 snapshot. Confirm the installed version and source date; do not present scan results as current HIG certification.

Use `--json` or SARIF for structured follow-up, baselines for new-issue gates, and `--fail-on` only under project policy. For each finding, retain tool version, rule ID, engine, and location, then classify:

- `confirmed`: source/runtime evidence supports an actionable issue
- `contextual`: validity depends on product, platform, or code context
- `false positive`: analyzer assumption does not apply

Watch for code-quality opinions labeled as HIG concerns, regex matches without semantic context, valid brand colors, intentional custom fonts, justified safe-area backgrounds, and framework/version changes. Use `--fix` only for authorized implementation; inspect every diff and rerun affected checks.

## 6. Re-verify

1. Re-run every failed or affected check.
2. Re-render the same window, OS, data, appearance, text size, and state.
3. Re-test Critical and Major paths first.
4. Check for regressions across another relevant platform, state, or input.
5. Re-fetch primary evidence if the fix depends on a disputed or current API.
6. Re-score only verified dimensions.
7. List untested platforms, OS versions, devices, inputs, states, and accessibility modes.

## Completion standard

Call the task complete only when requested changes are implemented, proportionate project checks pass, runtime or rendered evidence supports UI claims, authoritative claims link to current sources, and remaining limits are explicit. A clean scan, successful build, or attractive screenshot alone does not establish HIG alignment or ship readiness.
