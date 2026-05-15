#!/usr/bin/env python3
"""HTML updater — replaces only DATA constant, preserves all styling/images."""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent.parent
INDEX_HTML = ROOT / 'index.html'

def to_marathi(s):
    m = {'0':'०','1':'१','2':'२','3':'३','4':'४','5':'५','6':'६','7':'७','8':'८','9':'९'}
    return ''.join(m.get(c,c) for c in str(s))

def run(data):
    if not INDEX_HTML.exists():
        print(f'  ⚠ {INDEX_HTML} not found')
        return False
    html = INDEX_HTML.read_text(encoding='utf-8')
    new_data = 'const DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';'
    pat = re.compile(r'const\s+DATA\s*=\s*\[.*?\];', re.DOTALL)
    if not pat.search(html):
        print('  ✗ DATA constant not located')
        return False
    html = pat.sub(lambda m: new_data, html, count=1)
    
    # Update stat counters
    total = len(data)
    today_count = sum(1 for d in data if d.get('is_today'))
    dept_count = len(set(d['department'] for d in data))
    month_count = sum(1 for d in data if d.get('is_this_month'))
    
    INDEX_HTML.write_text(html, encoding='utf-8')
    print(f'  ✓ index.html updated: {total} docs, {today_count} today, {dept_count} depts')
    return True

if __name__ == '__main__':
    with open(ROOT / 'data' / 'grs.json', encoding='utf-8') as f:
        run(json.load(f))
