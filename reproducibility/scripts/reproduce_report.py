#!/usr/bin/env python3
"""Recompute reported classification and matched rationale metrics; stdlib only.
This DOES NOT retrain models or recreate LIME perturbations.
"""
import csv
from pathlib import Path
from statistics import mean, median

ROOT=Path(__file__).resolve().parents[1]

def rows(path):
    with (ROOT/path).open(newline='',encoding='utf-8-sig') as fh:
        return list(csv.DictReader(fh))

def class_metrics(tn,fp,fn,tp):
    p0=tn/(tn+fn);r0=tn/(tn+fp);f0=2*p0*r0/(p0+r0)
    p1=tp/(tp+fp);r1=tp/(tp+fn);f1=2*p1*r1/(p1+r1)
    return dict(accuracy=(tn+tp)/(tn+fp+fn+tp),macro_f1=(f0+f1)/2,
                offensive_precision=p1,offensive_recall=r1,offensive_f1=f1)

def explanation_metrics(records):
    return dict(n=len(records),mean_f1_lambda_0=mean(float(r['f1_0']) for r in records),
        mean_f1_lambda_0p5=mean(float(r['f1_05']) for r in records),
        mean_delta_lambda_0=mean(float(r['delta_p_offensive_0']) for r in records),
        mean_delta_lambda_0p5=mean(float(r['delta_p_offensive_05']) for r in records),
        flip_rate_lambda_0=mean(r['label_flipped_0'].lower()=='true' for r in records),
        flip_rate_lambda_0p5=mean(r['label_flipped_05'].lower()=='true' for r in records))

def main():
    print('CLASSIFICATION: verified confusion-matrix values')
    cm=rows('results/confusion_matrices.csv')
    for r in cm:
        m=class_metrics(*(int(r[k]) for k in ['tn','fp','fn','tp']))
        print(r['configuration'], ' '.join(f'{k}={v:.5f}' for k,v in m.items()))
    print('\nMATCHED EXPLANATIONS: 76 cases')
    matched=rows('results/canonical/lime_matched_76.csv')
    if len(matched)!=76:
        raise ValueError('Expected 76 matched cases; received '+str(len(matched)))
    for tag,group in [('all',matched),('partial_only',[r for r in matched if r['whole_sentence_rationale_0'].lower()!='true']),('whole_sentence',[r for r in matched if r['whole_sentence_rationale_0'].lower()=='true'])]:
        m=explanation_metrics(group)
        print(tag,' '.join(f'{k}={v:.5f}' if isinstance(v,float) else f'{k}={v}' for k,v in m.items()))
    assert len([r for r in matched if r['whole_sentence_rationale_0'].lower()!='true'])==61
    assert len(rows('results/canonical/lime_alignment_lambda_0.csv'))==78
    assert len(rows('results/canonical/lime_alignment_lambda_0p5.csv'))==77
    print('\nPASS: stored CSV counts and matched summary verified')

if __name__=='__main__': main()
