# Website Deployment Guide — Step by Step

**Goal:** Get your website live at `manitjain.com` with GitHub for version control.

---

## PART 1: Test Locally (5 minutes)

### Why it might not open when you double-click:
Your site uses React which needs a web server. Double-clicking the HTML file opens it as `file://` which blocks React from loading.

### Quick Fix — Test in Browser:

**Option A: Use Python (Mac/Linux):**
```bash
# Open Terminal, navigate to your website folder
cd /path/to/your/website/folder

# Start a simple web server
python3 -m http.server 8000

# Open browser to: http://localhost:8000
```

**Option B: Use VS Code Live Server:**
1. Install VS Code
2. Install "Live Server" extension
3. Right-click `index.html` → "Open with Live Server"

**Option C: Just deploy it (recommended)** — Skip local testing and go straight to deployment. You'll see it live in 5 minutes.

---

## PART 2: GitHub Setup (10 minutes)

### Step 1: Create GitHub Account
1. Go to https://github.com
2. Sign up (free account)
3. Verify email

### Step 2: Create Repository
1. Click the "+" icon (top right) → "New repository"
2. **Repository name:** `manitjain.github.io` (exactly this — it's special)
3. **Description:** "Personal website — Finance executive and strategic investor"
4. **Public** (keep it public)
5. **DO NOT** check "Add a README file"
6. Click "Create repository"

### Step 3: Upload Your Files

**Via Web Interface (Easiest):**
1. On your new repo page, click "uploading an existing file"
2. Drag these files into the upload box:
   - `index.html`
   - `README.md`
   - `CONTENT_GUIDE.md`
3. Scroll down, add commit message: "Initial commit: Personal website v1"
4. Click "Commit changes"

**Your site is now live at: `https://manitjain.github.io`** (Wait 2-3 minutes for first deploy)

---

## PART 3: Custom Domain Setup (15 minutes)

### Step 1: Buy Domain
1. Go to https://namecheap.com (or Google Domains, Cloudflare)
2. Search for: `manitjain.com`
3. Purchase ($8-12/year)
4. **Don't buy any add-ons** (hosting, email, etc. — you don't need them)

### Step 2: Configure DNS at Namecheap

1. Log into Namecheap
2. Go to Domain List → Click "Manage" next to `manitjain.com`
3. Click "Advanced DNS" tab
4. Delete all existing records
5. Add these 4 records:

**A Records (GitHub Pages IPs):**
```
Type: A Record | Host: @ | Value: 185.199.108.153 | TTL: Automatic
Type: A Record | Host: @ | Value: 185.199.109.153 | TTL: Automatic
Type: A Record | Host: @ | Value: 185.199.110.153 | TTL: Automatic
Type: A Record | Host: @ | Value: 185.199.111.153 | TTL: Automatic
```

**CNAME Record (www subdomain):**
```
Type: CNAME Record | Host: www | Value: manitjain.github.io | TTL: Automatic
```

6. Save all changes

### Step 3: Configure GitHub Pages for Custom Domain

1. Go to your GitHub repo: `https://github.com/yourusername/manitjain.github.io`
2. Click "Settings" (top menu)
3. Click "Pages" (left sidebar)
4. Under "Custom domain", enter: `manitjain.com`
5. Click "Save"
6. Wait 30 seconds, then check "Enforce HTTPS" (if available)

### Step 4: Add CNAME File

1. In your GitHub repo, click "Add file" → "Create new file"
2. Name it: `CNAME` (all caps, no extension)
3. File content (just one line):
```
manitjain.com
```
4. Commit the file

**Wait 10-30 minutes for DNS to propagate.**

Your site will be live at:
- `https://manitjain.com`
- `https://www.manitjain.com`
- `https://manitjain.github.io` (redirects to custom domain)

---

## PART 4: Future Updates (Every time you change content)

### Method 1: Edit Directly on GitHub (Easiest)

1. Go to your repo: `https://github.com/yourusername/manitjain.github.io`
2. Click `index.html`
3. Click the pencil icon (Edit)
4. Make your changes
5. Scroll down, add commit message: "Add new blog post about X"
6. Click "Commit changes"
7. **Your site updates automatically in 30-60 seconds**

### Method 2: Upload New Version

1. Download your edited `index.html` from your computer
2. Go to GitHub repo
3. Click `index.html` → Click trash icon to delete old version → Commit
4. Click "Add file" → "Upload files" → Upload new `index.html` → Commit

### Method 3: Git Command Line (For Frequent Updates)

**One-time setup:**
```bash
# Install Git (if not installed)
# Mac: brew install git
# Windows: Download from git-scm.com

# Navigate to your website folder
cd /path/to/your/website

# Initialize Git
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/manitjain.github.io.git
git push -u origin main
```

**Every time you make changes:**
```bash
# Make your edits to index.html

# Save and push
git add .
git commit -m "Add new investment memo"
git push

# Site updates in 30-60 seconds
```

---

## PART 5: Adding New Blog Posts

### Quick Reference:

1. Open `index.html` in any text editor
2. Find line ~200: `const blogPosts = [`
3. Copy the template from `CONTENT_GUIDE.md`
4. Paste your new post
5. Save file
6. Upload to GitHub (see Part 4)

**Example:**
```javascript
{
    id: 'palantir-analysis',
    category: 'Investment Memo',
    title: 'Palantir: Government moat meets AI acceleration',
    excerpt: 'Deep dive into PLTR's competitive position...',
    date: '2026-05-01',
    isPDF: false,
    content: `
        <h3>Your content here</h3>
        <p>With HTML formatting...</p>
    `
},
```

---

## PART 6: Updating Portfolio Date

**Monthly update:**

1. Open `index.html`
2. Find line ~350: `Last updated: April 2026`
3. Change to current month
4. Upload to GitHub

---

## TROUBLESHOOTING

### Site not loading?
- Wait 2-3 minutes after first GitHub upload
- Clear browser cache (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- Check GitHub Pages settings are enabled

### Custom domain not working?
- DNS takes 10-30 minutes to propagate (sometimes up to 24 hours)
- Check your DNS settings match exactly (case-sensitive)
- Make sure CNAME file exists in repo

### Changes not showing?
- Wait 60 seconds after commit
- Hard refresh browser (Cmd+Shift+R)
- Check commit went through on GitHub

### React not loading locally?
- Don't double-click HTML file
- Use a local server (see Part 1)
- Or just work directly on GitHub and view live site

---

## CHECKLIST

- [ ] GitHub account created
- [ ] Repository `manitjain.github.io` created
- [ ] Files uploaded (`index.html`, `README.md`, `CONTENT_GUIDE.md`)
- [ ] Site working at `https://manitjain.github.io`
- [ ] Domain `manitjain.com` purchased
- [ ] DNS records configured (4 A records + 1 CNAME)
- [ ] Custom domain added in GitHub Settings → Pages
- [ ] CNAME file added to repo
- [ ] HTTPS enabled
- [ ] Site live at `https://manitjain.com`

---

## QUICK LINKS

- Your GitHub repo: `https://github.com/yourusername/manitjain.github.io`
- GitHub Pages settings: `https://github.com/yourusername/manitjain.github.io/settings/pages`
- Your live site: `https://manitjain.com`
- Namecheap DNS: `https://ap.www.namecheap.com/domains/domaincontrolpanel/manitjain.com/advancedns`

---

## NEXT STEPS AFTER LAUNCH

1. **Add Google Analytics** (optional)
   - Get tracking ID from analytics.google.com
   - Add snippet to `<head>` in index.html

2. **Submit to Google Search Console**
   - Verify ownership
   - Submit sitemap
   - Monitor search performance

3. **Share on LinkedIn**
   - Post: "Just launched my personal site showcasing investment analysis and finance leadership insights: manitjain.com"

4. **Add to email signature**
   ```
   Manit Jain
   Senior Director, Finance Business Partnering
   Farfetch (Coupang)
   manitjain.com | LinkedIn
   ```

5. **Update monthly**
   - Add new blog posts
   - Update portfolio holdings date
   - Keep content fresh

---

**Need help?** Email manitjain87@gmail.com (that's you!)

---

**Estimated total time:** 30-45 minutes to go from zero to live site with custom domain.