#!/usr/bin/env python3
"""Summarize observed Skill ROI without inventing missing evidence."""
import argparse, csv, statistics
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'data'/'roi-ledger.csv'
p=argparse.ArgumentParser(); p.add_argument('--skill', default=''); p.add_argument('--mode', default=''); a=p.parse_args()
rows=list(csv.DictReader(LEDGER.open(encoding='utf-8')))
rows=[r for r in rows if (not a.skill or r['skill']==a.skill) and (not a.mode or r['mode']==a.mode)]
g=defaultdict(list)
for r in rows: g[(r['skill'],r['mode'])].append(r)
print(f'events={len(rows)}')
for (skill,mode),rs in sorted(g.items()):
    n=len(rs); success=sum(r['outcome']=='success' for r in rs)/n; corr=sum(int(r['correction']) for r in rs)/n; rework=sum(int(r['rework']) for r in rs)/n; route=sum(int(r['routing_ok']) for r in rs)/n; turns=statistics.median(int(r['turns']) for r in rs); ctx=statistics.mean(int(r['context_cost']) for r in rs)
    evidence='E0' if n==0 else ('E1' if n<3 else 'E2')
    if n>=3 and success>=0.9 and corr<=0.1 and rework<=0.1: evidence='E3-candidate'
    print(f'{skill}/{mode}: n={n} success={success:.2%} correction={corr:.2%} rework={rework:.2%} routing={route:.2%} median_turns={turns:g} context={ctx:.2f} evidence={evidence}')
