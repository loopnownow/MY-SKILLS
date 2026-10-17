# 03_research personal handoff

## Layout (2026-10-16)

- Top of `03_research/`: `SKILL.md`, `personal/`, `fill-protocol/`, `find-journal/`, `workflows/`.
- Former `literature/`, `design/`, `frontier/` single files → `personal/`.
- `clinical-translation/` → `personal/clinical-translation/` (whole pack).
- `fill-protocol/` stays at `03_research/fill-protocol/` (Bai / ownership path stability).
- `journal-patterns-2023-2026.md` merged into `personal/journal-selection.md`; old file archived under `D:\0del\03_research_reorg_20261016\`.

## Dual sync

Keep identical:

1. `C:\Users\loopn\.grok\skills\03_research`
2. `D:\0Grok\0doc\GitHub\MY-SKILLS\03_research`

## find-journal data split

| In MY-SKILLS `find-journal/data/2026/` | In 0doc `04-lab-reference\find-journal\data\2026\` |
|---|---|
| blacklist.csv / blacklist-names.csv | full-pool.csv |
| graylist.csv / graylist-names.csv | category-index.csv |
| whitelist-bmc-medicine.csv | layer1-*, layer2-*, layer2b-*, layer3-*, layer4-* |
| submission-urls.csv (URL write-back) | priority-compact.json |
| README.md, SUBMISSION_PRIVACY.md | publisher-fees.csv |

Runtime selection pools live in **0doc**. Skill pack keeps list gates only.

## Project submission history

选刊结果 / 已投杂志名单 live under **subproject folders**, e.g.:

```text
<project>/ref/journals-submitted.md
```

Do not store project submission history in MY-SKILLS. Lab-wide 投过 whitelist stays at `{find_journal_submission}\whitelist-submitted.csv`.

## Mounts

Do not edit `registry.yaml` / mounts-cap / fine-id paths from this reorg. Mounted ids (`lit-search`, `design-study`, …) unchanged.