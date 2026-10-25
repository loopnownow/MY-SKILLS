# Workflows (00)

Canonical SOP bodies for lab composites. **00 calls these files directly**; no second SOP tree lives under 03 or another seat.

| SOP | When | File |
|-----|------|------|
| statistics | image/ROI/features -> 02 HTML | `statistics.md` |
| sci-manuscript | HTML -> house draft -> pre-review / response | `sci-manuscript.md` |
| research-exploration-loop | research gaps / topic exploration | `research-exploration-loop.md` |
| review-isolation | review isolation / simulate->self/peer | `review-isolation.md` |
| question-to-reference | question -> evidence -> design -> data -> brief | `question-to-reference.md` |

**Session fine-id pick:** every independent run needs a fine-id pick. If the session lock already covers this task, reuse it. Otherwise run the 00 ask-each-run pick. Registry fine-id menu is the pick list; proposed ids are not pickable. Load only the ids picked this run. **Do not auto-load** all live ids.

Gate criteria: `00_orchestrator/gates.md`. 00 owns schedule / QC; SOP bodies stay here.
