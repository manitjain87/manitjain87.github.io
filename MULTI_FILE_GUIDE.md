# Multi-File Website Structure — Easy Content Management

## Why This Is Better

✅ **Each blog post = separate HTML file** — Edit one post without touching others  
✅ **Add new posts = create new file** — No risk of breaking the whole site  
✅ **Shared CSS/JS** — Change styles once, applies everywhere  
✅ **Better SEO** — Each post has its own URL and meta tags  
✅ **Easier collaboration** — Multiple people can work on different posts  

---

## File Structure

```
/
├── index.html              # Homepage (all sections + blog grid)
├── css/
│   └── style.css           # All styles (shared across pages)
├── js/
│   └── main.js             # Navigation & smooth scrolling
├── blog/
│   ├── _TEMPLATE.html      # Copy this for new posts
│   ├── mercadolibre-meli-memo.html
│   ├── ai-first-org-design.html
│   ├── dlocal-tradeoffs-munger.html
│   └── ... (add more as you write)
├── README.md
├── DEPLOYMENT_GUIDE.md
└── CONTENT_GUIDE.md
```

---

## How to Add a New Blog Post (5 minutes)

### Step 1: Create the Post File

1. Go to the `blog/` folder
2. Copy `_TEMPLATE.html`
3. Rename it: `your-post-slug.html` (e.g., `palantir-analysis.html`)
4. Open in any text editor

### Step 2: Fill in the Template

Replace these placeholders:

**In `<head>`:**
```html
<title>Your Post Title — Manit Jain</title>
<meta name="description" content="Your post excerpt here">
```

**In post header:**
```html
<div class="blog-category">Investment Memo</div>
<h1 class="blog-post-title">Your Post Title</h1>
<div class="blog-post-meta">April 6, 2026 · 8 min read</div>
```

**In content area (between comment markers):**
```html
<h3>Main Section</h3>
<p>Your paragraph text...</p>

<h4>Subsection</h4>
<ul>
    <li>Bullet point</li>
    <li>Another point</li>
</ul>
```

### Step 3: Add Card to Homepage

Open `index.html`, find the `<section id="writing">` section, and add:

```html
<a href="blog/your-post-slug.html" class="blog-card">
    <div class="blog-category">Investment Memo</div>
    <div class="blog-title">Your Post Title</div>
    <div class="blog-excerpt">Brief summary of your post...</div>
    <div class="blog-date">April 6, 2026</div>
</a>
```

### Step 4: Upload to GitHub

```bash
# Option A: Upload via web
# Go to GitHub → Upload files → Drag blog/your-post-slug.html and index.html

# Option B: Git command line
git add .
git commit -m "Add new post: Your Post Title"
git push
```

**Your new post is live in 60 seconds!**

---

## Content Formatting Guide

### Headings
```html
<h3>Main Section Heading</h3>
<h4>Subsection Heading</h4>
```

### Paragraphs
```html
<p>Your paragraph text here.</p>
```

### Lists
```html
<ul>
    <li>Bullet point</li>
    <li>Another point</li>
</ul>

<ol>
    <li>Numbered item 1</li>
    <li>Numbered item 2</li>
</ol>
```

### Bold & Italic
```html
<strong>Bold text</strong>
<em>Italic text</em>
```

### Links
```html
<a href="https://example.com">Link text</a>
```

### Quotes
```html
<blockquote>
This is a quote from someone important.
</blockquote>
```

### Tables
```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
    </tr>
</table>
```

### Highlighted Box (like the MercadoLibre note)
```html
<div style="margin-top: 40px; padding: 24px; background: var(--color-accent-light); border-left: 4px solid var(--color-accent); border-radius: 8px;">
    <p><strong>Note:</strong> Your highlighted text here.</p>
</div>
```

---

## Updating Existing Content

### To Edit a Blog Post:
1. Go to `blog/` folder
2. Open the HTML file you want to edit
3. Make your changes to the content
4. Save and upload to GitHub

### To Update Styles (applies to ALL pages):
1. Open `css/style.css`
2. Make your changes
3. Save and upload to GitHub
4. All pages update automatically

### To Update Navigation:
1. Open `js/main.js` (or edit navigation in any HTML file)
2. Make changes
3. Save and upload

---

## Example: Creating the Palantir Post

**1. Copy template:**
```bash
cp blog/_TEMPLATE.html blog/palantir-analysis.html
```

**2. Edit palantir-analysis.html:**
```html
<title>Palantir: Government moat meets AI acceleration — Manit Jain</title>
<meta name="description" content="Deep dive into PLTR's competitive position...">

<div class="blog-category">Investment Memo</div>
<h1 class="blog-post-title">Palantir: Government moat meets AI acceleration</h1>
<div class="blog-post-meta">May 1, 2026 · 10 min read</div>

<h3>The Thesis</h3>
<p>Palantir is...</p>
```

**3. Add to index.html (in the #writing section):**
```html
<a href="blog/palantir-analysis.html" class="blog-card">
    <div class="blog-category">Investment Memo</div>
    <div class="blog-title">Palantir: Government moat meets AI acceleration</div>
    <div class="blog-excerpt">Deep dive into PLTR's competitive position...</div>
    <div class="blog-date">May 1, 2026</div>
</a>
```

**4. Upload both files to GitHub**

Done!

---

## Benefits of This Structure

### Before (Single File):
- ❌ 1,383 lines in one file
- ❌ Easy to break everything while editing
- ❌ Hard to find specific posts
- ❌ Risk of syntax errors affecting whole site

### After (Multi-File):
- ✅ Each post ~100-200 lines
- ✅ Edit one post = zero risk to others
- ✅ Clear file organization
- ✅ Professional structure
- ✅ Easier to manage 50+ posts in future

---

## Testing Locally

**Problem:** Double-clicking HTML files doesn't work with the new structure (relative paths need a server).

**Solution:** Use Python web server:

```bash
# Navigate to your website folder
cd /path/to/your/website

# Start server
python3 -m http.server 8000

# Open browser to:
http://localhost:8000
```

Or just deploy to GitHub and test the live site.

---

## Deployment (No Changes)

The deployment process is **exactly the same** as before:

1. Upload entire folder to GitHub repository `manitjain.github.io`
2. GitHub Pages serves it automatically
3. Custom domain works the same way

**Important:** When uploading to GitHub, upload the **entire folder structure**:
- index.html
- css/ (folder)
- js/ (folder)
- blog/ (folder)

---

## Common Tasks

### Monthly Portfolio Update
**File:** `index.html`  
**Find:** `Last updated: April 2026`  
**Change:** Current month

### Add New Post
1. Copy `blog/_TEMPLATE.html` → `blog/new-post.html`
2. Fill in content
3. Add card to `index.html` in #writing section
4. Upload both files to GitHub

### Change Site Colors
**File:** `css/style.css`  
**Find:** `:root { --color-accent: #0F6E56; }`  
**Change:** To your preferred color

### Update Navigation
**File:** Any HTML file, find `<nav>` section  
**Or:** Edit `js/main.js` for behavior

---

## Quick Reference

**Homepage:** `index.html`  
**All styles:** `css/style.css`  
**Blog posts:** `blog/*.html`  
**New post template:** `blog/_TEMPLATE.html`  
**Example post:** `blog/mercadolibre-meli-memo.html`

---

## Next Steps

1. ✅ Structure is ready
2. ✅ One example post created (MercadoLibre)
3. ⏭️ Create remaining 9 blog posts using template
4. ⏭️ Deploy to GitHub
5. ⏭️ Set up custom domain

**Need help?** The template has detailed comments inside it!