#!/usr/bin/env python3
"""Check input CSV presence and common schema without printing original messages."""
import argparse,csv
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input-dir',default='data/raw')
    args=p.parse_args()
    root=Path(args.input_dir)
    for name in ['training_data.csv','TEST_WITHOUT_TRIGGERS.csv','TEST_WITH_TRIGGERS.csv']:
        path=root/name
        if not path.is_file():
            print('MISSING',path);continue
        with path.open(newline='',encoding='utf-8-sig') as stream:
            reader=csv.DictReader(stream)
            n=sum(1 for _ in reader)
            cols=reader.fieldnames or []
        print('FOUND',path,'rows',n,'columns',cols)
    print('Published corpus=977; experimental file total=780+196=976; reconcile source accounting separately.')
if __name__=='__main__':main()
