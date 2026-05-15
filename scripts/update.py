#!/usr/bin/env python3
"""
══════════════════════════════════════════════════════════════════════
  वंदे नागपूर · दैनिक auto-update scraper
══════════════════════════════════════════════════════════════════════
  सर्वस्व: CA श्रीकांत जगदीशप्रसाद दुबे · ९४०३ ५८६ ९००
  महामंत्री · भाजपा नागपूर महानगर

  Sources:
   1. gr.maharashtra.gov.in/1145/Government-Resolutions (सर्व विभाग)
   2. egazzete.mahaonline.gov.in (राजपत्र)
══════════════════════════════════════════════════════════════════════
"""
import json, re, sys, time
from pathlib import Path
from datetime import datetime
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / 'data' / 'grs.json'

GR_PORTAL = 'https://gr.maharashtra.gov.in/1145/Government-Resolutions'
GAZETTE_PORTAL = 'https://egazzete.mahaonline.gov.in/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0 Safari/537.36',
}

# Department mapping (Marathi name → code + icon)
DEPT_MAP = {
    'नगर विकास': ('UDD', '🏛️'),
    'ग्राम विकास': ('RDD', '🌾'),
    'महसूल': ('Revenue', '📜'),
    'सामाजिक न्याय': ('SJSA', '⚖️'),
    'इतर मागास': ('OBC', '🤝'),
    'अल्पसंख्याक': ('Minority', '🕌'),
    'कृषी': ('Agri', '🌾'),
    'सहकार': ('Coop', '🤝'),
    'शिक्षण': ('Edu', '📚'),
    'आरोग्य': ('Health', '🏥'),
    'महिला': ('WCD', '👩'),
    'कामगार': ('Labour', '👷'),
    'उद्योग': ('Industry', '🏭'),
    'सार्वजनिक बांधकाम': ('PWD', '🚧'),
    'जलसंपदा': ('WRD', '💧'),
    'अन्न': ('FCS', '🍚'),
    'गृह': ('Home', '🛡️'),
    'परिवहन': ('Transport', '🚌'),
    'वने': ('Forest', '🌳'),
    'क्रीडा': ('Sports', '🏏'),
    'पर्यटन': ('Tourism', '🎭'),
    'नियोजन': ('Planning', '📊'),
    'वित्त': ('Finance', '💰'),
}


def log(msg):
    print(f'[{datetime.utcnow().strftime("%H:%M:%S")}] {msg}', flush=True)


def fetch(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=45, verify=False)
            r.raise_for_status()
            return r.text
        except Exception as e:
            log(f'  [{attempt}/{retries}] Fetch failed: {e}')
            time.sleep(3)
    return None


def categorize(title):
    """Identify department from title text."""
    title_lower = title.lower()
    for key, (code, icon) in DEPT_MAP.items():
        if key in title:
            return key + ' विभाग', code, icon
    return 'इतर विभाग', 'Other', '📄'


def parse_date(text):
    m = re.search(r'(\d{1,2})[-./](\d{1,2})[-./](\d{2,4})', text)
    if not m:
        return '', None
    d, mo, y = m.groups()
    if len(y) == 2:
        y = '20' + y
    try:
        year = int(y)
    except:
        year = None
    return f'{int(d):02d}-{int(mo):02d}-{y}', year


def scrape_gr_portal():
    log('► gr.maharashtra.gov.in scrape करत आहे...')
    html = fetch(GR_PORTAL)
    if not html:
        return []
    soup = BeautifulSoup(html, 'lxml')
    docs = []
    seen = set()
    
    # GR portal has tables/lists with PDF links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if not (href.lower().endswith('.pdf') or 'download' in href.lower()):
            continue
        if href in seen:
            continue
        seen.add(href)
        
        title = a.get_text(' ', strip=True)
        if not title or len(title) < 10:
            parent = a.find_parent(['tr', 'li', 'div'])
            if parent:
                title = parent.get_text(' ', strip=True)
        if len(title) < 10:
            continue
        
        full_url = href if href.startswith('http') else f'https://gr.maharashtra.gov.in{href}'
        date_str, year = parse_date(title)
        dept_mr, dept_code, dept_icon = categorize(title)
        
        docs.append({
            'title_mr': title[:250],
            'date': date_str,
            'date_iso': f'{year}-01-01' if year else '',
            'year': year,
            'department': dept_mr,
            'department_code': dept_code,
            'department_icon': dept_icon,
            'department_en': dept_code,
            'doc_type': 'GR',
            'doc_type_mr': 'शासन निर्णय',
            'gr_number': '',
            'pdf_url': full_url,
            'source': 'GR Portal',
        })
    
    log(f'  ✓ GR Portal: {len(docs)} दस्तऐवज सापडले')
    return docs


def main():
    log('═' * 60)
    log('  वंदे नागपूर · दैनिक अद्ययावत scraper')
    log('═' * 60)
    
    # Load existing
    if DATA_FILE.exists():
        with open(DATA_FILE, encoding='utf-8') as f:
            current = json.load(f)
        log(f'सध्याचे dataset: {len(current)} दस्तऐवज')
    else:
        current = []
        log('नवीन dataset तयार करत आहे')
    
    existing_urls = {d['pdf_url'] for d in current}
    
    # Scrape
    try:
        new_docs = scrape_gr_portal()
    except Exception as e:
        log(f'⚠ Scrape error: {e}')
        return 0
    
    # Filter only new ones
    truly_new = [d for d in new_docs if d['pdf_url'] not in existing_urls]
    
    if not truly_new:
        log('\n✓ कोणतीही नवीन GRs नाहीत. सर्व up-to-date.')
        return 0
    
    log(f'\n⚡ {len(truly_new)} नवीन GRs सापडले:')
    for d in truly_new[:10]:
        log(f'  + [{d["department_code"]}] {d["title_mr"][:60]}')
    
    # Assign IDs
    max_id = 0
    for d in current:
        m = re.search(r'(\d+)$', d.get('id', ''))
        if m:
            max_id = max(max_id, int(m.group(1)))
    
    today = datetime.utcnow()
    for i, d in enumerate(truly_new):
        d['id'] = f'MH-{max_id + i + 1:04d}'
        d['is_today'] = True
        d['is_this_week'] = True
        d['is_this_month'] = True
        # Set today's date if no date parsed
        if not d.get('date'):
            d['date'] = today.strftime('%d-%m-%Y')
            d['date_iso'] = today.strftime('%Y-%m-%d')
            d['year'] = today.year
            d['month'] = today.month
    
    # Reset "is_today" flags on existing docs
    for d in current:
        d['is_today'] = False
    
    merged = truly_new + current
    
    # Save
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    log(f'\n✓ Dataset अद्ययावत: {len(merged)} दस्तऐवज एकूण')
    
    # Rebuild HTML
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
