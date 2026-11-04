# Setswana MRP: public reproducibility supplement

This directory supplements the IEEE Access manuscript **Masked Rationale Prediction for Explainable Offensive Language Detection in Setswana**. It contains source notebooks (outputs cleared), experiment settings, and **aggregate** results. It does **not** include row-level evaluation outputs, raw dataset messages, or annotated trigger spans; those require a separate permission/privacy review.

## Experiments
- `lambda=0`: custom PuoBERTa classification-only control
- `lambda=0.5`: same custom architecture with rationale-guided masked-token reconstruction
- Five-fold development CV, seeds `42, 0, 13`; final seed `42`; two independent ten-epoch final training configurations
- Pretrained backbone: `dsfsi/PuoBERTa`

## Contents
- `notebooks/archival/` contains original **code snapshots**, without saved cell outputs. These are audit records, not independently rerun reproducibility guarantees.
- `notebooks/corrected_candidate/` isolates a candidate repair for an observed reference to the wrong Trainer object. It is **not** a verified reproduction of final paper results.
- `configs/` records seed/parameter settings.
- `results/confusion_matrices.csv` and `results/summary_metrics.csv` supply aggregate figures; see paper for complete results.
- `scripts/validate_public_results.py` validates the aggregated figures. `scripts/reproduce_report.py` is provided for running with withheld per-example CSVs after an approved data release.

## Reproducing training
Training data CSVs and checkpoint identifiers are **not yet included**. Set the input paths in the archival notebooks; their Colab Drive paths are original examples and must be adapted. Code should be audited for compatibility and the Trainer-reference issue before rerunning. The notebooks contain preprocessing and evaluation logic used in the research but are not guaranteed one-click reproducible.

## Scientific limitations
- The published source dataset contains 977 entries while experimental files account for 976. This discrepancy remains under review.
- Gold-trigger word overlap uses sets of unique word identities, not exact-position spans.
- Neither mean LIME F1 nor counterfactual deletion alone proves explanation faithfulness.
- These final runs use one seed per condition; CV seeds and final training seed must not be confused.

## Public-release policy
Do not commit row-level results, annotated text, model checkpoints, private input data, API secrets or private Colab Drive files without explicit verification of sharing rights, anonymisation and provenance. The `.gitignore` files provide partial safeguards, not a substitute for review.
