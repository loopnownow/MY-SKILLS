#!/usr/bin/env python3
"""Append one observable Skill-ROI event to the local ledger."""
import argparse, csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'data'/'roi-ledger.csv'
FIELDS=['date','skill','mode','task_id','outcome','correction','rework','routing_ok','turns','context_cost','benefit_note']
p=argparse.ArgumentParser()
p.add_argument('--date', required=True); p.add_argument('--skill', required=True); p.add_argument('--mode', required=True)
p.add_argument('--task-id', required=True); p.add_argument('--outcome', choices=['success','partial','failed'], required=True)
p.add_argument('--correction', type=int, choices=[0,1], required=True); p.add_argument('--rework', type=int, choices=[0,1], required=True)
p.add_argument('--routing-ok', type=int, choices=[0,1], required=True); p.add_argument('--turns', type=int, required=True)
p.add_argument('--context-cost', type=int, choices=range(4), required=True); p.add_argument('--benefit-note', default='')
a=p.parse_args()
with LEDGER.open('a',newline='',encoding='utf-8') as f:
    csv.DictWriter(f,fieldnames=FIELDS).writerow({'date':a.date,'skill':a.skill,'mode':a.mode,'task_id':a.task_id,'outcome':a.outcome,'correction':a.correction,'rework':a.rework,'routing_ok':a.routing_ok,'turns':a.turns,'context_cost':a.context_cost,'benefit_note':a.benefit_note})
print(f'Recorded: {a.skill}/{a.mode} -> {a.outcome}')
