# 🪷 वंदे नागपूर

### महाराष्ट्र शासन — सर्व विभागांचे शासन निर्णय, परिपत्रके व राजपत्र एका ठिकाणी

[![Auto-Update](https://img.shields.io/badge/अद्ययावत-दैनिक-success)]()
[![Free](https://img.shields.io/badge/सेवा-१००%25%20मोफत-orange)]()
[![Marathi](https://img.shields.io/badge/भाषा-मराठी-blue)]()

---

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                    ★ वंदे नागपूर ★                                 ║
║                                                                    ║
║              भाजपा नागपूर महानगर — प्रस्तुत                       ║
║       "सबका साथ · सबका विकास · सबका विश्वास"                       ║
║                                                                    ║
║       तयार करणारे: CA श्रीकांत जगदीशप्रसाद दुबे                    ║
║                   महामंत्री · भाजपा नागपूर महानगर                  ║
║       मुख्य मार्गदर्शक: श्री सुनील मित्रा (OSD, CM महाराष्ट्र)     ║
║                                                                    ║
║       📞 ९४०३ ५८६ ९००                                              ║
║       📧 bjpdpnagpur@gmail.com                                     ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 मुख्य वैशिष्ट्ये

- ✅ **सर्व २६+ विभागांचे GRs** — एका ठिकाणी
- ✅ **दैनिक auto-update** — दर रोज सकाळी ८ वा. IST (automatic GitHub Actions)
- ✅ **१००% मोफत** — कोणतेही शुल्क, ad नाही, registration नाही
- ✅ **मराठी UI** — पूर्णपणे देवनागरी, मराठी संख्या (०-९)
- ✅ **Mobile-friendly** — phone/tablet/desktop सर्वत्र
- ✅ **Search + Filter** — विभाग, प्रकार, कालावधी, GR क्रमांक
- ✅ **WhatsApp Share** — एका tap मध्ये कार्यकर्त्यांना forward
- ✅ **🔥 आजच्या ठळक बातम्या** — top GRs prominently displayed
- ✅ **Today's badge** — नवीन GRs वर "नवीन" pulse animation

---

## 🌐 Live URL

GitHub Pages deploy केल्यानंतर:

```
https://YOUR_USERNAME.github.io/vande-nagpur/
```

(YOUR_USERNAME ऐवजी आपले GitHub username — उदा. `cashrikantdubey`)

---

## 📦 Repository Structure

```
vande-nagpur/
├── index.html                          ← मुख्य Dashboard (GitHub Pages serves this)
├── README.md                           ← हे file
├── DEPLOYMENT_GUIDE.md                 ← Step-by-step Marathi setup guide
│
├── data/
│   └── grs.json                        ← सर्व GRs metadata (auto-updated daily)
│
├── scripts/
│   ├── update.py                       ← दैनिक scraper (gr.maharashtra.gov.in)
│   ├── build_html.py                   ← HTML मध्ये नवीन data inject करते
│   └── requirements.txt                ← Python dependencies
│
└── .github/workflows/
    └── daily-update.yml                ← GitHub Actions cron (8 AM IST)
```

---

## 🔄 दैनिक Auto-Update कसे काम करते?

```
दर रोज सकाळी ८:०० (IST) automatically
      │
      ▼
GitHub Actions सुरू होते
      │
      ▼
scripts/update.py चालते
      ├─► gr.maharashtra.gov.in scrape
      └─► नवीन GRs compare वर्तमान dataset शी
      │
      ▼
नवीन सापडले?
      ├─ हो ──► data/grs.json update
      │        └─► index.html मध्ये नवीन data
      │        └─► auto-commit + push to GitHub
      │        └─► Live site आपोआप updated
      │
      └─ नाही ─► "सर्व up-to-date" log
```

**आपल्याला रोज काहीही करावे लागत नाही.** Lifetime मोफत.

---

## 📊 Coverage

### विभाग (Departments)

| क्र | विभाग | Icon |
|---|------|------|
| 1 | नगर विकास विभाग | 🏛️ |
| 2 | ग्राम विकास विभाग | 🌾 |
| 3 | महसूल विभाग | 📜 |
| 4 | सामाजिक न्याय व विशेष सहाय्य | ⚖️ |
| 5 | इतर मागास बहुजन कल्याण | 🤝 |
| 6 | अल्पसंख्याक विकास | 🕌 |
| 7 | कृषी विभाग | 🌾 |
| 8 | सहकार विभाग | 🤝 |
| 9 | शालेय शिक्षण व क्रीडा | 📚 |
| 10 | उच्च व तंत्रशिक्षण | 🎓 |
| 11 | सार्वजनिक आरोग्य | 🏥 |
| 12 | वैद्यकीय शिक्षण | ⚕️ |
| 13 | महिला व बाल विकास | 👩 |
| 14 | कामगार विभाग | 👷 |
| 15 | उद्योग, ऊर्जा व कामगार | 🏭 |
| 16 | सार्वजनिक बांधकाम | 🚧 |
| 17 | जलसंपदा | 💧 |
| 18 | अन्न, नागरी पुरवठा | 🍚 |
| 19 | गृह विभाग | 🛡️ |
| 20 | परिवहन | 🚌 |
| 21 | वने विभाग | 🌳 |
| 22 | क्रीडा व युवक कल्याण | 🏏 |
| 23 | पर्यटन व सांस्कृतिक कार्य | 🎭 |
| 24 | नियोजन विभाग | 📊 |
| 25 | वित्त विभाग | 💰 |
| 26 | नगर परिषदा | 🏘️ |

---

## 🛠️ Setup करायचे आहे का?

**विस्तृत Marathi मार्गदर्शक**: [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md)

मुख्य पायऱ्या:
1. GitHub account तयार करा / login करा
2. नवीन repository (`vande-nagpur`) तयार करा (Public)
3. या folder मधील सर्व files upload करा
4. **Settings → Pages** → `main` branch → Save
5. **Actions tab** → Enable workflows
6. ५-१० मिनिटांत URL live होईल!

---

## ⚖️ अधिकृत स्रोत व कायदेशीर माहिती

हे dashboard खालील **अधिकृत शासकीय स्रोतांचे** GRs केवळ **सोयीसाठी एकत्र संकलित** करते:

1. **महाराष्ट्र शासन GR Portal** — https://gr.maharashtra.gov.in/1145/Government-Resolutions
2. **महाराष्ट्र राजपत्र** — https://egazzete.mahaonline.gov.in/

> **टीप**: हे dashboard व्यावसायिक हेतू नसून फक्त जनसेवेसाठी आहे. कोणत्याही GR/PDF चे copyright त्या-त्या शासकीय विभागाचे आहे.

---

## 📞 संपर्क

**तयार करणारे**: CA श्रीकांत जगदीशप्रसाद दुबे
- 📱 मो. / WhatsApp: **९४०३ ५८६ ९००**
- 📧 Email: **bjpdpnagpur@gmail.com**
- 🏛️ महामंत्री · भाजपा नागपूर महानगर
- 🎓 सनदी लेखापाल (CA) · ICAI · ३० वर्षांचा अनुभव

**मुख्य मार्गदर्शक व संकलन**: श्री सुनील मित्रा
- OSD · माननीय मुख्यमंत्री महाराष्ट्र राज्य
- मुख्यमंत्री कार्यालय, मंत्रालय, मुंबई

---

```
═══════════════════════════════════════════════════════════════════
  © २०२६ · वंदे नागपूर · भाजपा नागपूर महानगर
  "जनसेवा हीच ईश्वरसेवा"
  जय हिंद · जय महाराष्ट्र · वंदे मातरम्
═══════════════════════════════════════════════════════════════════
```
