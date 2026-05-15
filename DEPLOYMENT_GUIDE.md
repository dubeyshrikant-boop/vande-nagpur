# 🚀 वंदे नागपूर — GitHub Deployment मार्गदर्शक

## संपूर्ण मराठी step-by-step मार्गदर्शक · २० मिनिटांत Live!

---

## 📋 आपल्याकडे काय आहे?

हे folder आहे आपल्या **वंदे नागपूर** dashboard साठी GitHub Repository structure. एकदा हे GitHub वर upload केले की:

- ✅ कोणीही `https://USERNAME.github.io/vande-nagpur/` या URL वर dashboard पाहू शकेल
- ✅ **दर रोज सकाळी ८ वा** automatically scrape — नवीन GRs आढळल्यास dashboard update होईल
- ✅ कोणत्याही manual मेहनतीशिवाय — **lifetime मोफत**

---

## 🎯 Step-by-Step Deployment (२० मिनिटे)

### Step 1: GitHub Account तयार करा (नाही असेल तर)

1. https://github.com वर जा
2. **"Sign up"** वर click — email + password
3. Username निवडा (उदा. `cashrikantdubey` किंवा `bjpdpnagpur`)
4. Verification email check करा

### Step 2: नवीन Repository तयार करा

1. GitHub वर login केल्यावर वरच्या उजव्या कोपऱ्यातील **`+`** icon → **"New repository"**
2. भरा:
   - **Repository name**: `vande-nagpur`
   - **Description**: `वंदे नागपूर — महाराष्ट्र शासन निर्णय भांडार · भाजपा नागपूर महानगर`
   - **Public** निवडा ⚠️ (आवश्यक — GitHub Pages साठी)
   - **"Add a README file"** टिक न करा (आपल्याकडे आधीच आहे)
3. **"Create repository"** वर click

### Step 3: सर्व Files Upload करा

1. नवीन repository page वर **"uploading an existing file"** link किंवा **"Add file"** → **"Upload files"** वर click
2. **या folder मधील सर्व files drag-and-drop करा**:
   - `index.html` ⭐ (मुख्य dashboard)
   - `README.md`
   - `DEPLOYMENT_GUIDE.md`
   - `data/` folder (grs.json सह)
   - `scripts/` folder (update.py, build_html.py, requirements.txt)
   - `.github/` folder ⚠️ (hidden — drag-drop मध्ये miss होऊ शकते)
3. खाली scroll → **"Commit changes"** वर click

> ⚠️ **टीप — `.github` folder upload करण्यासाठी**:
> 
> Drag-drop मध्ये hidden folders दिसत नाहीत. म्हणून:
> 1. Browser मध्ये **"Add file"** → **"Create new file"** click करा
> 2. File path मध्ये लिहा: `.github/workflows/daily-update.yml` (GitHub automatically folders तयार करेल)
> 3. ZIP मधील `daily-update.yml` चे content paste करा
> 4. **"Commit changes"** click

### Step 4: GitHub Pages सुरू करा

1. Repository मध्ये **"Settings"** tab वर click (वरच्या navigation मध्ये)
2. डाव्या sidebar मध्ये खाली scroll करून **"Pages"** वर click
3. **"Build and deployment"** section मध्ये:
   - **Source**: "Deploy from a branch" निवडा
   - **Branch**: `main` निवडा
   - **Folder**: `/ (root)` ठेवा
   - **"Save"** वर click
4. ५-१० मिनिटे थांबा. URL तयार होईल:
   ```
   https://USERNAME.github.io/vande-nagpur/
   ```
   (USERNAME = आपले GitHub username)

### Step 5: Auto-Update Workflow Enable करा

1. Repository मध्ये **"Actions"** tab वर click
2. GitHub प्रथमच विचारेल: **"I understand my workflows, go ahead and enable them"** — Enable करा
3. डाव्या sidebar मध्ये **"दैनिक अद्ययावत · Daily Auto-Update"** workflow दिसेल
4. आत्ता एकदा manual test करा:
   - त्या workflow वर click → **"Run workflow"** dropdown → **"Run workflow"** confirm
   - ३-५ मिनिटांत run पूर्ण होईल. हिरवा ✓ दिसेल = सर्व ठीक
5. नंतर **दर रोज सकाळी ८:०० (IST)** automatic चालेल

> 🎉 **पूर्ण झाले!** आता दर रोज नवीन GRs आपोआप जोडले जातील.

---

## 🌐 आपला URL Live झाला!

आता हा link सर्वांना share करा:

```
https://USERNAME.github.io/vande-nagpur/
```

### WhatsApp Forward Message (Ready-to-Copy)

```
🪷 *वंदे नागपूर — मोफत सेवा*

महाराष्ट्र शासनाचे सर्व शासन निर्णय (GRs),
परिपत्रके आणि राजपत्र एका ठिकाणी — पूर्णपणे *मोफत*.

🌐 *लिंक*:
https://USERNAME.github.io/vande-nagpur/

✅ २६+ विभागांचे GRs
✅ दैनिक auto-update
✅ Search + filter + WhatsApp share
✅ Mobile-friendly

— *भाजपा नागपूर महानगर*

तयार करणारे:
*CA श्रीकांत जगदीशप्रसाद दुबे*
महामंत्री · भाजपा नागपूर महानगर
📞 ९४०३ ५८६ ९००
📧 bjpdpnagpur@gmail.com

मुख्य मार्गदर्शक व संकलन:
*श्री सुनील मित्रा*
OSD, मुख्यमंत्री महाराष्ट्र राज्य

जय हिंद · जय महाराष्ट्र · वंदे मातरम्
```

---

## 🎨 Custom Domain (Optional)

`vandenagpur.in` किंवा `bjpdpnagpur.in` सारखा domain हवा असल्यास:

1. **Domain register**: GoDaddy / Namecheap / BigRock — ₹५००-१००० /वर्ष
2. GitHub Repository → Settings → Pages → **"Custom domain"** मध्ये domain लिहा
3. Registrar कडे DNS मध्ये CNAME record जोडा:
   - Name: `@` (किंवा `www`)
   - Value: `USERNAME.github.io`
4. ३०-६० मिनिटांत domain live होईल

---

## 🆘 Troubleshooting

### "Site can't be reached" error
- ✋ १० मिनिटे थांबा — GitHub Pages deploy होण्यासाठी वेळ लागतो
- Settings → Pages — verify Source = `main`, Folder = `/ (root)`
- URL right आहे का check करा (case-sensitive)

### Actions workflow fail होतेय
- Actions tab → failed run वर click → log पहा
- सामान्य कारण: गव्हर्नमेंट website temporarily down — पुढच्या आठवड्यात आपोआप retry होईल
- Manual retry: workflow वर click → "Re-run failed jobs"

### URL वर photos दिसत नाहीत
- सर्व photos base64 म्हणून embedded आहेत
- Browser cache clear करा (Ctrl+F5 / Cmd+Shift+R)

### कोणतेही नवीन GRs नाही येत
- gr.maharashtra.gov.in वर त्या दिवशी नवीन GRs publish नसतील
- Workflow log check करा — दिसेल "सर्व up-to-date"

---

## 📊 Site Analytics (Optional)

किती लोक site वापरत आहेत हे track करायचे आहे?

1. **Google Analytics** account तयार करा (free)
2. GA tracking code मिळवा
3. index.html च्या `<head>` मध्ये paste करा
4. GitHub वर commit करा

---

## 📞 मदत हवी?

GitHub setup मध्ये अडचण आल्यास, मला WhatsApp करा:

**CA श्रीकांत जगदीशप्रसाद दुबे**
📞 ९४०३ ५८६ ९००
📧 bjpdpnagpur@gmail.com

---

```
═══════════════════════════════════════════════════════════════════
  © वंदे नागपूर · सहकार चळवळीला वंदन
  CA श्रीकांत जगदीशप्रसाद दुबे · आवृत्ती १.०
═══════════════════════════════════════════════════════════════════
```
