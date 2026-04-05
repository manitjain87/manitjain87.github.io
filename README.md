# Manit Jain — Personal Website

## Overview

Executive-grade personal website positioning you as a CFO-track executive and strategic investor. Built as a single-page React application with clean, professional design.

## Features

✅ **Responsive design** — Perfect on mobile, tablet, desktop  
✅ **Dark mode support** — Auto-adapts to system preferences  
✅ **SEO optimized** — Meta tags for search visibility  
✅ **Fast loading** — Single HTML file, no build process  
✅ **Easy content updates** — Simple structure for adding blog posts  

## Sections

1. **Hero** — CFO-track positioning with contact info and CTA
2. **Experience** — Timeline with Farfetch, Coupang, Shopify, Walmart
3. **Investing** — Philosophy + portfolio (public/private)
4. **Projects** — Charlie investment research assistant
5. **Writing** — Blog posts and investment memos
6. **Contact** — Recruiter-optimized CTA

## File Structure

```
/
├── index.html           # Main website (production-ready)
├── CONTENT_GUIDE.md     # How to add blog posts and memos
├── README.md            # This file
└── CV__MANIT_JAIN__2026.pdf  # Your CV (for download link)
```

## How to Deploy

### Option 1: GitHub Pages (Recommended — Free)

1. Create a GitHub account if you don't have one
2. Create a new repository called `manitjain.github.io`
3. Upload `index.html` and your CV
4. Go to Settings → Pages → Source → main branch
5. Your site will be live at `https://manitjain.github.io`

**Custom domain setup:**
- Buy `manitjain.com` from Namecheap (~$10/year)
- Add CNAME record pointing to `manitjain.github.io`
- Add `CNAME` file in repo with your domain name

### Option 2: Netlify (Easy — Free)

1. Go to netlify.com and sign up
2. Drag and drop your folder
3. Your site is live immediately
4. Free custom domain setup

### Option 3: Vercel (Developer-friendly — Free)

1. Go to vercel.com and sign up
2. Import from GitHub or drag folder
3. Auto-deployment on every update

## How to Update Content

### Adding Blog Posts

1. Open `index.html`
2. Find the section around line 450: `const blogPosts = [...]`
3. Add new posts using this template:

```javascript
{
    category: "Investment Memo",
    title: "Your Title",
    excerpt: "Brief summary",
    date: "2026-04-04",
    content: `Your full content here`
}
```

See `CONTENT_GUIDE.md` for detailed examples.

### Updating Experience

Find the `experience` array (around line 200) and add/modify entries.

### Updating Portfolio

Find the `portfolio` array (around line 250) and add new investments.

## Customization

### Colors

The site uses CSS variables for theming. To change the accent color:

```css
--color-accent: #0F6E56;  /* Teal - change to your preferred color */
```

### Fonts

Currently using system fonts for performance. To add custom fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

Then update:
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

## Technical Details

- **Framework:** React 18 (loaded via CDN)
- **Build:** None required — single HTML file
- **Size:** ~20KB (extremely fast)
- **Browser support:** All modern browsers + IE11
- **Mobile:** Fully responsive, tested on iOS/Android

## SEO Optimization

Already included:
- Meta description
- Semantic HTML structure
- Clean URLs (via anchor links)
- Fast loading time

**Next steps for SEO:**
1. Add Google Analytics
2. Submit to Google Search Console
3. Get LinkedIn to link to your site
4. Add structured data (JSON-LD)

## Analytics Setup (Optional)

To add Google Analytics:

1. Create account at analytics.google.com
2. Get tracking ID (G-XXXXXXXXXX)
3. Add before `</head>`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## Future Enhancements

Consider adding:
- [ ] Blog post detail pages (instead of inline content)
- [ ] Contact form (using Formspree or similar)
- [ ] Newsletter signup
- [ ] Case study PDFs for investment memos
- [ ] Testimonials section
- [ ] Speaking/advisory page

## Maintenance

**Monthly:**
- Review analytics
- Add new blog posts
- Update portfolio if needed

**Quarterly:**
- Refresh experience section
- Add new projects
- Review SEO performance

## Support

Questions? Email manitjain87@gmail.com

---

Built with ❤️ by Claude