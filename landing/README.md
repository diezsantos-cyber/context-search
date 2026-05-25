# Landing Page

Simple HTML landing page for Context Search.

## Deploy Options

### Option 1: Vercel (Recommended - Free)

1. Create account at https://vercel.com
2. Click "New Project"
3. Import from Git or upload `landing/` folder
4. Deploy
5. Get URL: `context-search.vercel.app`

### Option 2: Netlify (Free)

1. Drag and drop `landing/` folder to https://app.netlify.com/drop
2. Get instant URL
3. (Optional) Add custom domain later

### Option 3: GitHub Pages (Free)

1. Create repo `yourusername.github.io`
2. Upload `index.html`
3. Enable GitHub Pages in settings
4. Live at `yourusername.github.io`

## Before Deploy: Update Stripe Link

Line 327 in `index.html`:

```html
<a href="https://buy.stripe.com/YOUR_STRIPE_LINK" ...>
```

Replace `YOUR_STRIPE_LINK` with your actual Stripe payment link after creating it.

## Test Locally

```bash
cd landing/
python3 -m http.server 8080
# Visit: http://localhost:8080
```

---

**Next Step:** Create Stripe product + payment link, then update the button href.
