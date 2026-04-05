# Content Management Guide

This file shows you how to add blog posts and investment memos (as PDFs or full articles) to your website.

## Quick Start: Adding Content

### Step 1: Open index.html
Find the section around line 200 that starts with:
```javascript
// Blog posts data - ADD YOUR CONTENT HERE
const blogPosts = [
```

### Step 2: Add Your Content
Copy one of the templates below and paste it into the array.

---

## Template 1: Full Blog Post (Shows on Site)

Use this for LinkedIn posts, articles, or shorter investment memos you want readers to view directly on your site.

```javascript
{
    id: 'unique-slug-here',  // Used in URL, no spaces
    category: 'Investment Memo',  // or 'Finance Leadership', 'Market Analysis'
    title: 'Your Title Here',
    excerpt: 'A brief 1-2 sentence summary for the card',
    date: '2026-04-05',  // YYYY-MM-DD format
    isPDF: false,
    content: `
        <h3>Section Heading</h3>
        <p>Your content here. You can use HTML:</p>
        
        <ul>
            <li><strong>Bold items</strong> with details</li>
            <li>Bullet points for lists</li>
        </ul>
        
        <p>Multiple paragraphs work great.</p>
        
        <h4>Subheading</h4>
        <p>More content...</p>
    `
}
```

---

## Template 2: PDF Case Study (Links to PDF)

Use this for longer investment memos you want to provide as downloadable PDFs.

```javascript
{
    id: 'shopify-memo-2024',
    category: 'Investment Memo',
    title: 'Shopify: Commerce infrastructure thesis',
    excerpt: 'Deep dive into platform economics, merchant cohorts, and path to $500B GMV',
    date: '2024-11-15',
    isPDF: true,
    pdfUrl: '/memos/shopify-investment-memo.pdf'  // Place PDF in same folder as index.html
}
```

**To add PDF:**
1. Save your PDF in the same folder as `index.html`
2. Name it clearly: `shopify-memo.pdf`
3. Reference it in `pdfUrl: '/shopify-memo.pdf'`

---

## Full Example: Investment Memo as Blog Post

```javascript
{
    id: 'shopify-commerce-infrastructure',
    category: 'Investment Memo',
    title: 'Shopify: Commerce infrastructure for the internet',
    excerpt: 'Platform economics, merchant retention, and the path to $500B GMV',
    date: '2024-11-15',
    isPDF: false,
    content: `
        <h3>Investment Thesis</h3>
        
        <p>Shopify is building the commerce operating system for independent businesses globally. 
        The platform has evolved from a simple storefront builder to a full-stack commerce infrastructure 
        spanning payments, fulfillment, capital, and marketing.</p>
        
        <h3>Unit Economics</h3>
        
        <ul>
            <li><strong>Merchant cohort retention:</strong> 95%+ after year 1, driven by switching costs and ecosystem lock-in</li>
            <li><strong>GMV per merchant:</strong> Growing 20%+ annually as businesses scale and attach rates improve</li>
            <li><strong>Revenue per merchant:</strong> $3,500+ annually, up 30%+ YoY via payments/capital/fulfillment attach</li>
        </ul>
        
        <h3>Competitive Moat</h3>
        
        <p>Three structural advantages compound over time:</p>
        
        <ul>
            <li><strong>Developer ecosystem:</strong> 8,000+ apps create switching costs — migrating off Shopify means rebuilding integrations</li>
            <li><strong>Multi-sided network:</strong> Merchants attract developers, developers build apps, apps attract more merchants</li>
            <li><strong>Technical founder:</strong> Tobi Lutke ensures product velocity and platform coherence others can't match</li>
        </ul>
        
        <h3>Valuation Framework</h3>
        
        <p>Current P/S of 12x appears expensive vs. SaaS peers at 8x, but justified by:</p>
        
        <ul>
            <li>25%+ revenue growth vs. 15% peer median</li>
            <li>Path to 20%+ FCF margins (currently 15%)</li>
            <li>TAM expansion into B2B commerce and offline retail</li>
        </ul>
        
        <h3>Key Risks</h3>
        
        <ul>
            <li><strong>Amazon competition:</strong> Could bundle commerce tools into AWS/marketplace</li>
            <li><strong>Regulation:</strong> Payment processing faces increasing regulatory scrutiny</li>
            <li><strong>Macro sensitivity:</strong> SMB spending correlates with economic cycles</li>
        </ul>
        
        <h3>Position Sizing</h3>
        
        <p>Core holding at 8% of portfolio. Will add on pullbacks below $60.</p>
    `
}
```

---

## Full Example: LinkedIn Post

```javascript
{
    id: 'commercial-finance-partnership',
    category: 'Finance Leadership',
    title: 'Why most finance teams fail at commercial partnering',
    excerpt: 'The gap between financial reporting and business partnership — and how to close it',
    date: '2026-03-20',
    isPDF: false,
    content: `
        <p>I've rebuilt finance teams at Farfetch, Coupang, and Shopify. The pattern is always the same.</p>
        
        <p>Most finance teams are stuck in <strong>reporting mode</strong>:</p>
        <ul>
            <li>Monthly variance analysis</li>
            <li>Budget vs. actuals</li>
            <li>Headcount tracking</li>
        </ul>
        
        <p>Elite finance teams operate in <strong>partnering mode</strong>:</p>
        <ul>
            <li>What's the payback on this customer acquisition campaign?</li>
            <li>Should we expand to Germany or France first?</li>
            <li>What's our LTV:CAC by cohort and channel?</li>
        </ul>
        
        <h3>How to Make the Shift</h3>
        
        <p>The difference isn't skill — it's mandate and muscle memory. Here's the playbook:</p>
        
        <h4>1. Embed finance in commercial reviews</h4>
        <p>Don't wait for month-end close. Sit in weekly pipeline reviews, product launches, 
        marketing planning. Show up where decisions happen.</p>
        
        <h4>2. Build bottom-up forecasts</h4>
        <p>Top-down targets tell you what the CEO wants. Bottom-up models tell you what's 
        actually achievable based on pipeline, cohorts, and conversion rates.</p>
        
        <h4>3. Track unit economics, not just P&L</h4>
        <p>Revenue and EBITDA are lagging indicators. CAC payback, NRR, and contribution 
        margin are leading indicators that drive decisions.</p>
        
        <h3>The Proof</h3>
        
        <p>When I joined Farfetch, finance was a reporting function. Within 6 months, we were 
        driving pricing strategy, marketing budget allocation, and market entry decisions.</p>
        
        <p>The EBITDA swing from −$31M to profitable wasn't because of better accounting. 
        It was because finance became a commercial partner to the CEO and business leaders.</p>
    `
}
```

---

## Updating Portfolio Last Updated Date

Find this section in `index.html` (around line 350):

```javascript
<div style={{fontSize: '14px', color: 'var(--color-text-tertiary)'}}>
    Last updated: April 2026  // ← Change this monthly
</div>
```

Simply update the month/year each time you modify your portfolio holdings.

---

## Content Categories

Choose from these categories for consistency:

- `Investment Memo` — Deep dives on portfolio companies
- `Finance Leadership` — CFO/finance insights
- `Market Analysis` — Sector trends, macro views
- `Turnaround Insights` — Operational finance, restructuring
- `LinkedIn Post` — Shorter thought leadership

---

## HTML Formatting Guide

Inside the `content` field, you can use:

**Headings:**
```html
<h3>Main Section</h3>
<h4>Subsection</h4>
```

**Paragraphs:**
```html
<p>Your paragraph text here.</p>
```

**Lists:**
```html
<ul>
    <li>Bullet point</li>
    <li><strong>Bold point</strong> with regular text</li>
</ul>
```

**Links:**
```html
<a href="https://example.com">Link text</a>
```

**Bold/Italic:**
```html
<strong>Bold text</strong>
<em>Italic text</em>
```

---

## Pro Tips

1. **Write in Google Docs first** — easier to edit, then paste into template
2. **Keep excerpts punchy** — 1-2 sentences max, shows on card
3. **Use subheadings** — breaks up long memos, aids scanning
4. **Date everything** — shows you're actively writing
5. **Mix formats** — Some PDFs, some on-site posts
6. **Start with 6-8 pieces** — Enough to show range, not overwhelming

---

## Where to Add in Code

In `index.html`, find line ~200:

```javascript
const blogPosts = [
    // Existing posts here...
    
    // ADD YOUR NEW POSTS HERE ↓
    {
        id: 'your-new-post',
        category: 'Investment Memo',
        title: 'Your Title',
        // ... rest of template
    },
    
];
```

---

## Need Help?

Email manitjain87@gmail.com