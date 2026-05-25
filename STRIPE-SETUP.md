# Stripe Setup Guide - Step by Step

## Part 1: Create Stripe Account (5 min)

### Step 1: Sign Up
1. Go to https://stripe.com
2. Click "Sign up" (top right)
3. Enter:
   - Email
   - Full name
   - Country
   - Password
4. Click "Create account"

### Step 2: Verify Email
1. Check your email
2. Click verification link
3. Return to Stripe dashboard

### Step 3: Business Information (Optional for now)
- You can skip this initially and complete later
- For testing, Stripe works without full verification
- To receive real payments, you'll need to complete business profile

---

## Part 2: Enable Test Mode (Already enabled by default)

- Top right toggle should say "Test mode"
- All setup below will be in test mode first
- We'll switch to live mode after testing

---

## Part 3: Create Product (5 min)

### Step 1: Go to Products
1. Left sidebar → Click "Products"
2. Click "Add product" button (top right)

### Step 2: Product Details
Fill in:

**Product information:**
- Name: `Context Search - Beta Access`
- Description (optional): `Semantic code search for AI agents. Includes 1 repo, 50K symbols, 100 searches/day, email support.`

**Pricing:**
- Price: `49.00`
- Currency: `USD`
- Billing period: `Monthly` (dropdown)
- Recurring: ✅ checked

**Optional fields (leave as default):**
- Tax behavior: Not collecting tax
- Free trial: None (we can add later if needed)

### Step 3: Save
Click "Save product" (bottom right)

✅ **Product created!** Note the product ID (starts with `prod_...`)

---

## Part 4: Create Payment Link (5 min)

### Step 1: Create Link
1. Still on Products page
2. Find your "Context Search - Beta Access" product
3. Click the three dots ⋯ next to it
4. Select "Create payment link"

### Step 2: Configure Link

**Checkout settings:**
- After payment: Choose "Show a confirmation page" (default)
  - Or add custom URL: `https://yourlandingpage.com/success`

**Collect customer information:**
- ✅ Email address (checked)
- Optional: Name, Phone

**Allow promotion codes:**
- ❌ Leave unchecked for now (can enable later for discounts)

**Quantity:**
- ❌ "Adjustable quantity" unchecked (fixed 1 subscription)

### Step 3: Create Link
Click "Create link" (bottom right)

### Step 4: Copy Payment Link
- Stripe shows you the payment link
- Format: `https://buy.stripe.com/test_XXXXXXXXX` (test mode)
- **COPY THIS LINK** — we need it for the landing page

Example:
```
https://buy.stripe.com/test_14k29q0OL5hy3qU9AA
```

✅ **Payment link created!**

---

## Part 5: Test the Payment Link (3 min)

### Step 1: Open Payment Link
- Paste the link in your browser
- You should see Stripe checkout page
- Shows: "Context Search - Beta Access" $49/mo

### Step 2: Test Purchase
Use Stripe test card:
- Card number: `4242 4242 4242 4242`
- Expiry: Any future date (e.g., `12/26`)
- CVC: Any 3 digits (e.g., `123`)
- Name: Any name
- Email: Your email

### Step 3: Complete Test Purchase
- Click "Subscribe"
- Should see success message
- Check your email — you'll get test receipt

### Step 4: Verify in Stripe Dashboard
1. Go to Payments (left sidebar)
2. You should see the test payment
3. Status: "Succeeded"

✅ **Test payment works!**

---

## Part 6: Update Landing Page with Link (2 min)

### Find Your Payment Link
In Stripe:
1. Products → Your product
2. Click three dots ⋯
3. "Copy payment link"

### Update index.html

Open `/root/context-search/landing/index.html`

Find line ~327 (search for "YOUR_STRIPE_LINK"):

**BEFORE:**
```html
<a href="https://buy.stripe.com/YOUR_STRIPE_LINK" class="cta-button" style="margin-top: 30px;">
```

**AFTER:**
```html
<a href="https://buy.stripe.com/test_14k29q0OL5hy3qU9AA" class="cta-button" style="margin-top: 30px;">
```
(Use YOUR actual link, not this example)

### Save and Test
1. Save the file
2. Visit landing page
3. Click "Start Beta Now" button
4. Should open Stripe checkout

✅ **Landing page connected to Stripe!**

---

## Part 7: Email Automation (Manual for Beta)

### When someone pays (Test mode):

**You'll receive:**
- Stripe email notification
- Customer's email in Stripe dashboard

**What to do:**
1. Go to Stripe → Customers
2. Find the new customer
3. Note their email
4. Manually email them:

```
Subject: Your Context Search API Key - Welcome!

Hi [Customer Name],

Thanks for joining Context Search beta! 🎉

Here's your API access:

API Key: beta-key-[UNIQUE_ID]
API URL: https://context-search-production.up.railway.app

Quick Start:
1. Zip your Python repo
2. Index: curl -X POST https://[API_URL]/index -H "X-API-Key: [KEY]" -F "file=@repo.zip"
3. Search: curl -X POST https://[API_URL]/search -H "X-API-Key: [KEY]" -d '{"query":"your search","repo_id":"[ID]"}'

Full docs: https://[API_URL]/docs

Questions? Just reply to this email.

Best,
Pollux
Context Search
```

### Generate Unique API Keys:
```bash
# In your server
python3 -c "import uuid; print('beta-key-' + str(uuid.uuid4())[:8])"
# Example output: beta-key-a3f8c2d1
```

Then add that key to Railway environment variables:
```
API_KEYS=demo-key-123,beta-key-a3f8c2d1,beta-key-[next_customer]
```

---

## Part 8: Switch to Live Mode (When Ready)

### After Testing Works:

1. **Complete Stripe Account Verification:**
   - Settings → Account
   - Complete business details
   - Add bank account for payouts

2. **Activate Live Mode:**
   - Toggle from "Test mode" to "Live mode" (top right)

3. **Create Live Product:**
   - Repeat Part 3-4 in Live mode
   - Will get new payment link (without "test_" prefix)

4. **Update Landing Page:**
   - Replace test link with live link

5. **Update Environment Variable:**
   - Railway: Change API_KEYS to real production keys

---

## Security Best Practices

### API Key Management:
- Generate unique key per customer
- Never reuse keys
- Store securely in Railway env vars
- Consider key rotation after 90 days

### Stripe Webhooks (Later):
For automation, set up webhook to:
1. Listen for `checkout.session.completed`
2. Auto-generate API key
3. Auto-send welcome email via SendGrid/Mailgun
4. Add key to database/env

We'll add this after first 5 customers to validate manually first.

---

## Summary Checklist

- [ ] Created Stripe account
- [ ] Verified email
- [ ] Created product: "Context Search - Beta Access" $49/mo
- [ ] Created payment link
- [ ] Tested with card 4242...
- [ ] Received test payment in dashboard
- [ ] Updated landing page with payment link
- [ ] Tested landing page button → Stripe checkout works

**Once all checked: Ready to receive real payments! 🚀**

---

## Next Steps After Stripe Setup:

1. Deploy landing page (Vercel/Netlify)
2. Push GitHub repo (if not done)
3. Deploy API to Railway
4. Test full flow end-to-end
5. Start outreach to first customers

---

**Need help with any step? Let me know where you're stuck.**
