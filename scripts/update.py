#!/usr/bin/env python3
"""
══════════════════════════════════════════════════════════════════════
  वंदे नागपूर · DIRECT scraper for gr.maharashtra.gov.in
══════════════════════════════════════════════════════════════════════
  सर्वस्व: CA श्रीकांत जगदीशप्रसाद दुबे
  महामंत्री · भाजपा नागपूर महानगर · 9403 586 900

  Source: https://gr.maharashtra.gov.in/1145/Government-Resolutions
  (DIRECT scrape from OFFICIAL Maharashtra GR Portal — no third-party!)
══════════════════════════════════════════════════════════════════════
"""
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / 'data' / 'grs.json'

GR_LIST_URL = 'https://gr.maharashtra.gov.in/1145/Government-Resolutions'
PDF_URL_BASE = 'https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/Marathi/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'mr,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'no-cache',
}

DEPT_MAP = {
    'कृषी': ('Agri', '🌾'),
    'पशुसंवर्धन': ('Agri', '🌾'),
    'सहकार': ('Coop', '🤝'),
    'पणन': ('Coop', '🤝'),
    'वस्त्रोद्योग': ('Coop', '🤝'),
    'महसूल': ('Revenue', '📜'),
    'वन': ('Forest', '🌳'),
    'गृह': ('Home', '🛡️'),
    'गृहनिर्माण': ('Housing', '🏘️'),
    'उद्योग': ('Industry', '🏭'),
    'उर्जा': ('Industry', '⚡'),
    'कामगार': ('Labour', '👷'),
    'वित्त': ('Finance', '💰'),
    'नियोजन': ('Planning', '📊'),
    'पाणीपुरवठा': ('WaterSupply', '🚰'),
    'जलसंपदा': ('WRD', '💧'),
    'जलसंधारण': ('Soil', '💧'),
    'मृद': ('Soil', '🌱'),
    'सार्वजनिक आरोग्य': ('Health', '🏥'),
    'वैद्यकीय': ('MedEd', '⚕️'),
    'शालेय शिक्षण': ('SchoolEdu', '📚'),
    'क्रीडा': ('SchoolEdu', '🏏'),
    'उच्च व तंत्र शिक्षण': ('HTE', '🎓'),
    'सामाजिक न्याय': ('SJSA', '⚖️'),
    'अल्पसंख्याक': ('Minority', '🕌'),
    'इतर मागास': ('OBC', '🤝'),
    'आदिवासी': ('Tribal', '🌿'),
    'दिव्यांग': ('PWD', '♿'),
    'महिला': ('WCD', '👩'),
    'अन्न': ('FCS', '🍚'),
    'सामान्य प्रशासन': ('GAD', '🏛️'),
    'नगर विकास': ('Urban', '🏛️'),
    'ग्राम विकास': ('RuralDev', '🌾'),
    'सार्वजनिक बांधकाम': ('PublicWorks', '🚧'),
    'पर्यटन': ('Tourism', '🎭'),
    'सांस्कृतिक': ('Tourism', '🎭'),
    'मराठी भाषा': ('Marathi', '📖'),
    'कौशल्य': ('Skill', '🛠️'),
    'विधी': ('Law', '⚖️'),
    'न्याय': ('Law', '⚖️'),
    'पर्यावरण': ('Environment', '🌿'),
    'इलेक्ट्रॉनिक्स': ('IT', '💻'),
    'माहिती तंत्रज्ञान': ('IT', '💻'),
    'संसदीय': ('Parliamentary', '🏛️'),
}


def log(msg):
    print(f'[{datetime.utcnow().strftime("%H:%M:%S")}] {msg}', flush=True)


def categorize(dept):
    for key, (code, icon) in DEPT_MAP.items():
        if key in dept:
            return code, icon
    return 'Other', '📄'


def fetch_page():
    log(f'► Fetching {GR_LIST_URL}')
    session = requests.Session()
    session.headers.update(HEADERS)
    
    for attempt in range(1, 4):
        try:
            r = session.get(GR_LIST_URL, timeout=60, verify=False)
            log(f'  Attempt {attempt}: HTTP {r.status_code} ({len(r.text)} bytes)')
            if r.status_code == 200:
                return r.text
        except Exception as e:
            log(f'  Attempt {attempt} failed: {e}')
        time.sleep(5 * attempt)
    return None


def parse_grs(html):
    soup = BeautifulSoup(html, 'lxml')
    grs = []
    
    for row in soup.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) < 6:
            continue
        
        try:
            number_cell = cells[0].get_text(strip=True)
            if not number_cell.replace('.', '').isdigit():
                continue
            
            department = cells[1].get_text(strip=True)
            title = cells[2].get_text(strip=True)
            doc_id = cells[3].get_text(strip=True)
            date_str = cells[4].get_text(strip=True)
            
            pdf_link = row.find('a', href=re.compile(r'\.pdf', re.I))
            if not pdf_link:
                continue
            # BULLETPROOF: Construct URL directly from doc_id, no relative URL issues
            pdf_url = f'{PDF_URL_BASE}{doc_id}.pdf'
            
            date_parts = date_str.split('-')
            if len(date_parts) != 3:
                continue
            d, m, y = date_parts
            
            dept_code, icon = categorize(department)
            
            grs.append({
                'title_mr': title,
                'date': date_str,
                'date_iso': f'{y}-{m.zfill(2)}-{d.zfill(2)}',
                'year': int(y),
                'month': int(m),
                'department': department,
                'department_code': dept_code,
                'department_icon': icon,
                'department_en': dept_code,
                'doc_type': 'GR',
                'doc_type_mr': 'शासन निर्णय',
                'gr_number': doc_id,
                'pdf_url': pdf_url,
                'source': 'gr.maharashtra.gov.in',
            })
        except Exception:
            continue
    
    return grs


def main():
    log('═' * 60)
    log('  वंदे नागपूर · DIRECT scrape from gr.maharashtra.gov.in')
    log('═' * 60)
    
    if DATA_FILE.exists():
        with open(DATA_FILE, encoding='utf-8') as f:
            current = json.load(f)
        log(f'सध्याचे dataset: {len(current)} GRs')
    else:
        current = []
        log('नवीन dataset तयार करत आहे')
    
    existing_ids = {g.get('gr_number', '') for g in current if g.get('gr_number')}
    
    html = fetch_page()
    if not html:
        log('⚠ Could not fetch page')
        return 1
    
    new_grs = parse_grs(html)
    log(f'  ✓ Parsed {len(new_grs)} GRs from official portal')
    
    if not new_grs:
        log('⚠ No GRs parsed - check parser')
        return 1
    
    truly_new = [g for g in new_grs if g['gr_number'] not in existing_ids]
    
    if not truly_new:
        log('\n✓ कोणतीही नवीन GR नाही. सर्व up-to-date.')
        return 0
    
    log(f'\n⚡ {len(truly_new)} नवीन GRs:')
    for g in truly_new[:10]:
        log(f'  + [{g["department_code"]}] {g["title_mr"][:60]}')
    
    today = datetime.utcnow().strftime('%Y-%m-%d')
    for g in truly_new:
        g['is_today'] = (g['date_iso'] == today)
        g['is_this_week'] = True
        g['is_this_month'] = True
    
    for g in current:
        g['is_today'] = False
    
    max_id = 0
    for g in current:
        match = re.search(r'(\d+)$', g.get('id', 'MH-0000'))
        if match:
            max_id = max(max_id, int(match.group(1)))
    
    for i, g in enumerate(truly_new):
        g['id'] = f'MH-{max_id + i + 1:04d}'
    
    merged = truly_new + current
    
    # BULLETPROOF: Normalize ALL URLs (reconstruct from doc_id to fix any bad URLs)
    fixed = 0
    for g in merged:
        doc_id = g.get('gr_number', '')
        if doc_id and doc_id.isdigit():
            correct_url = f'{PDF_URL_BASE}{doc_id}.pdf'
            if g.get('pdf_url', '') != correct_url:
                g['pdf_url'] = correct_url
                fixed += 1
    if fixed:
        log(f'  ✓ Normalized {fixed} URLs (fixed malformed entries)')
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    log(f'\n✓ Dataset: {len(merged)} GRs एकूण')
    
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        import build_html
        build_html.run(merged)
    except Exception as e:
        log(f'⚠ Build issue: {e}')
    
    log('═' * 60)
    return 0


if __name__ == '__main__':
    sys.exit(main())
