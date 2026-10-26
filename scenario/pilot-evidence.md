# Four week pilot evidence

All values and comments below are invented for learning. They are not Cursor telemetry or measured effects of Cursor. Before and pilot periods each cover four weeks of small Python maintenance work in the same squad, but different work items. Severity mix, task complexity and staffing have not been controlled. This is a descriptive comparison, not a causal study.

| Indicator | Before period | Pilot period | Definition |
|---|---:|---:|---|
| Eligible changes | 20 | 24 | Changes meeting the stated small-maintenance scope |
| Changes with complete review evidence | 12 | 21 | Plan, diff, actual tests and human review all recorded |
| Median time from first commit to approval | 10 hours | 8 hours | Median across eligible changes, from internal review records |
| Changes reopened within 7 days | 2 | 4 | Each change counts at most once |
| Escaped severe incidents | 0 | 1 | Severe incidents linked by incident review to eligible changes |
| Cursor users active during the period | Not collected | 9 of 12 enabled | Fictional usage signal for the pilot cohort |
| Respondents reporting less repeated setup | Not collected | 6 of 8 respondents | Optional survey, four people did not respond |

Pilot interview notes: one developer found the shared procedure easy to reuse. A reviewer says one generated change had complete-looking evidence that omitted a failing check. Another developer could not find the skill because they opened a parent folder.

Proposed scenario gates, set before examining results: at least 85% complete evidence, no increase in reopened-change rate, zero unresolved severe incidents, and a named maintainer plus support route. These are fictional management choices, not universal thresholds or GitHub recommendations.

The severe incident remains unresolved at this review. Choose expand, adapt or pause and specify scope, immediate owner, missing evidence and a dated re-entry condition. Distinguish adoption, workflow quality, delivery outcome and risk. You may challenge the proposed thresholds but must give a reason and cannot retrospectively redefine success to conceal the incident.
