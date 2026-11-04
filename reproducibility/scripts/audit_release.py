#!/usr/bin/env python3
"""Conservative privacy scan: counts potential signals; not a release clearance."""
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TEXT_KEYS=('text','token','span','gold','lime','hl','content','sentence')
PATS={
    'email':re.compile(r'(?i)\b[a-z0-9_.+\-]+@[a-z0-9\-]+(?:\.[a-z0-9\-]+)+\b'),
    'url':re.compile(r'(?i)(?:https?://|www\.)\S+'),
    'handle':re.compile(r'(?<!\w)@[A-Za-z0-9_]{2,}'),
    'possible_phone':re.compile(r'(?<!\d)(?:\+?267[ -]?)?[37]\d{6,7}(?!\d)'),
}

def main():
    for path in sorted((ROOT/'results').rglob('*.csv')):
        counts={k:0 for k in PATS}
        with path.open(newline='',encoding='utf-8-sig') as f:
            rows=csv.DictReader(f)
            for r in rows:
                value=' '.join(str(v) for k,v in r.items() if any(t in k.lower() for t in TEXT_KEYS))
                for kind,patt in PATS.items():
                    counts[kind]+=bool(patt.search(value))
        print(path.relative_to(ROOT),'potential_issues=',counts)
    print('CAUTION: automated patterns cannot detect names, contextual identification, or licensing issues.')
if __name__=='__main__':main()
