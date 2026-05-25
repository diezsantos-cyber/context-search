# Day 3 Checklist - Deploy + Landing

**Goal:** API live on Railway + Landing page with Stripe

---

## Part 1: Push to GitHub (15 min)

### If you don't have a GitHub repo yet:

```bash
# On GitHub.com:
# 1. Create new repo "context-search" (private)
# 2. Copy the repo URL

# In terminal:
cd /root/context-search
git remote add origin https://github.com/YOUR_USERNAME/context-search.git
git branch -M main
git push -u origin main
```

### If repo already exists:

```bash
cd /root/context-search
git push
```

---

## Part 2: Deploy to Railway (30 min)

### 2.1 Create Railway Account
1. Go to https://railway.app
2. Sign in with GitHub
3. Allow Railway access to repos

### 2.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `context-search` repo
4. Railway auto-detects Python
5. Click "Deploy"

### 2.3 Set Environment Variables
1. Go to project → Variables tab
2. Add variables:
   ```
   OPENAI_API_KEY = sk-proj-...
   API_KEYS = beta-key-001,beta-key-002,beta-key-003
   PORT = 8000
   ```
3. Save

### 2.4 Wait for Deploy
- Usually takes 2-3 minutes
- Watch build logs for errors

### 2.5 Get Public URL
1. Go to Settings → Domains
2. Click "Generate Domain"
3. Copy URL: `context-search-production.up.railway.app`

### 2.6 Test Deployed API
```bash
# Replace with your Railway URL
export API_URL="https://context-search-production.up.railway.app"

# Health check
curl $API_URL/health

# Should return: {"status":"healthy"}
```

✅ **Checkpoint:** API is live and responding

---

## Part 3: Landing Page (2-3 hours)

### Option A: HTML + Vercel (recommended - free)

I can create a simple HTML page, you deploy to Vercel:

**What the page needs:**
- Hero: "98% Fewer Tokens for AI Agents"
- Problem: "AI agents waste millions of tokens with grep"
- Solution: "Semantic code search powered by embeddings"
- Pricing: "$49/mo Beta Access - Lifetime lock"
- CTA: "Get Started" button → Stripe checkout

### Option B: Carrd (faster - $19/year)

1. Go to https://carrd.co
2. Use "Startup" template
3. Customize:
   - Headline: "Context Search - 98% Fewer Tokens"
   - Subhead: "Semantic code search for AI agents"
   - Button: "Buy Beta Access" → links to Stripe
4. Publish to custom domain

### Which option do you prefer?

---

## Part 4: Stripe Setup (1-2 hours)

### 4.1 Create Stripe Account
1. Go to https://stripe.com
2. Sign up
3. Complete business info

### 4.2 Create Product
1. Dashboard → Products → Add product
2. Name: "Context Search - Beta Access"
3. Price: $49/mo recurring
4. Save

### 4.3 Create Checkout Page
1. Go to product → Create payment link
2. Mode: Subscription
3. Success URL: `https://yourlandingpage.com/success`
4. Copy payment link
5. Add link to landing page button

### 4.4 Test Purchase (Test Mode)
1. Use test card: 4242 4242 4242 4242
2. Any future date, any CVC
3. Complete checkout
4. Verify in Stripe dashboard

✅ **Checkpoint:** Can complete test purchase

---

## Part 5: Email Automation (1 hour)

### Simple Version (Manual for now)

**When someone pays:**
1. You get Stripe email notification
2. Manually email them:
   ```
   Subject: Your Context Search API Key

   Hi [name],

   Thanks for joining Context Search beta!

   Your API key: beta-key-XXX
   API URL: https://context-search-production.up.railway.app

   Quick Start:
   1. Upload your repo as .zip
   2. Use /docs for API reference
   3. Reply to this email for support

   - Pollux
   ```

### Automated Version (Later)

Use Stripe webhook → send email via SendGrid/Mailgun

---

## Part 6: Test End-to-End (30 min)

### Full Flow Test:
1. Visit landing page ✅
2. Click "Buy Beta" ✅
3. Complete Stripe checkout ✅
4. Receive email with API key ✅
5. Test API with that key ✅

---

## Success Criteria for Day 3

- [ ] Code pushed to GitHub
- [ ] API deployed on Railway
- [ ] Railway URL works: `/health` returns 200
- [ ] Landing page live
- [ ] Stripe checkout working (test mode)
- [ ] Can complete full purchase flow

**If all checked: Ready for Day 4-7 (outreach + customers)**

---

## Estimated Time: 5-6 hours total

- GitHub push: 15 min
- Railway deploy: 30 min  
- Landing page: 2-3 hours
- Stripe: 1-2 hours
- Testing: 30 min

---

**Where are you stuck or what should I help with next?**
