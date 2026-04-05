# Website Launch Checklist

## Phase 1: GitHub (10 min)
- [ ] Create GitHub account at github.com
- [ ] Create new repository named: `manitjain.github.io` (exactly this)
- [ ] Make it Public
- [ ] Upload `index.html`, `README.md`, `CONTENT_GUIDE.md`
- [ ] Verify site works at: https://manitjain.github.io (wait 2 min)

## Phase 2: Domain (15 min)
- [ ] Buy `manitjain.com` at namecheap.com ($8-12/year)
- [ ] Go to Namecheap → Domain List → Manage → Advanced DNS
- [ ] Delete all existing records
- [ ] Add 4 A Records pointing to:
  - 185.199.108.153
  - 185.199.109.153
  - 185.199.110.153
  - 185.199.111.153
- [ ] Add 1 CNAME Record: www → manitjain.github.io
- [ ] Save DNS changes

## Phase 3: Connect Domain to GitHub (5 min)
- [ ] Go to GitHub repo → Settings → Pages
- [ ] Enter custom domain: `manitjain.com`
- [ ] Click Save
- [ ] Create new file named `CNAME` (no extension)
- [ ] File content: `manitjain.com` (just one line)
- [ ] Commit the CNAME file
- [ ] Enable "Enforce HTTPS" (wait 5 min for it to appear)

## Phase 4: Wait & Verify (10-30 min)
- [ ] Wait 10-30 minutes for DNS propagation
- [ ] Test: https://manitjain.com (should load your site)
- [ ] Test: https://www.manitjain.com (should also work)
- [ ] Verify HTTPS (green padlock in browser)

## You're Live! 🎉

---

## For Future Updates:

### Adding New Content:
1. Go to GitHub repo → Click `index.html` → Click pencil (Edit)
2. Find line ~200: `const blogPosts = [`
3. Add your new post using CONTENT_GUIDE.md template
4. Scroll down → Add commit message → Commit changes
5. Site updates automatically in 60 seconds

### Monthly Portfolio Update:
1. Edit `index.html` on GitHub
2. Find: `Last updated: April 2026`
3. Change to current month
4. Commit changes

---

## Emergency Contacts:
- GitHub Support: support.github.com
- Namecheap Support: namecheap.com/support
- Your email: manitjain87@gmail.com

---

**Total Time:** ~30-45 minutes from start to live site