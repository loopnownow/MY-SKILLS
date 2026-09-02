#!/usr/bin/env python3
"""Score a proposed Skill evolution using the repository's benefit rubric.

Usage:
  python harvest_score.py --impact 3 --frequency 2 --reliability 2 --reuse 3 --maintenance 1 --context 1
"""
import argparse

p = argparse.ArgumentParser()
p.add_argument('--impact', type=int, choices=range(4), required=True)
p.add_argument('--frequency', type=int, choices=range(4), required=True)
p.add_argument('--reliability', type=int, choices=range(4), required=True)
p.add_argument('--reuse', type=int, choices=range(4), required=True)
p.add_argument('--maintenance', type=int, choices=range(4), required=True)
p.add_argument('--context', type=int, choices=range(4), required=True)
a = p.parse_args()
score = a.impact + a.frequency + a.reliability + a.reuse - a.maintenance - a.context
if score >= 6:
    decision = 'prioritize / retain'
elif score >= 3:
    decision = 'retain if evidence continues'
elif score >= 0:
    decision = 'observe / simplify / archive'
else:
    decision = 'revise / rollback'
print(f'priority_score={score}')
print(f'decision={decision}')
