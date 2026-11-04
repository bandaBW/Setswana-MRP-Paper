# Reproducibility status (accurate as packaged)

| Material | Status | Notes |
|---|---|---|
| Classification matrices | Included | Counts transcribed from verified manuscript comparison; not original prediction exports |
| LIME alignment per-example outputs | Included | 78 lambda=0 and 77 lambda=0.5 |
| Matched analysis | Included | 76 common correctly classified offensive cases; 61 partial-span cases |
| Rationale deletion outputs | Included | 78 and 77 offensive true positives |
| Intermediate parsed/joined CSVs | Included | Some include extra unmatched rows/diagnostic joins; preserve for auditing |
| Experiment seeds and hyperparameters | Included | From notebook configurations; CV seeds 42,0,13; final seed 42 |
| Source development and holdout files | Missing | Must supply authorized original CSVs |
| Exact checkpoint weights, revisions | Missing | Must archive/hash |
| Full original environment freeze | Missing | `requirements.txt` is indicative, not a lockfile |
| Reproducibility of lambda=0.5 final run | Unverified | Archived notebook references wrong trainer; corrected *candidate* included |
| Independent prospective validation | Not performed | Holdout has been examined repeatedly |

`python scripts/reproduce_report.py` confirms metrics *from saved outputs*, not from retraining. This distinction should be explicit in the manuscript's Data and Code Availability statement.
