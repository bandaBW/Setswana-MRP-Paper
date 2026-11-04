#!/usr/bin/env python3
"""Check public aggregate outputs without loading unpublished Setswana texts."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with (root/'results/confusion_matrices.csv').open(newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==2, 'Expected exactly two configurations'
for row in rows:
    cm=[int(row[k]) for k in ('tn','fp','fn','tp')]
    assert sum(cm)==196, f'Unexpected holdout count: {row}'
    acc=(cm[0]+cm[3])/196
    print(row['configuration'],'confusion:',cm,'accuracy:',round(acc,6))
with (root/'results/summary_metrics.csv').open(newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
assert any(r['metric']=='lime_mean_f1' for r in rows)
print('Public aggregate file OK:',len(rows),'metrics')
print('Note: this does not independently reproduce private row-level outputs.')
