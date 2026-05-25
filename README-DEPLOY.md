# Deploy Guide - Railway

## Step 1: Prepare for Railway

Railway needs:
- `requirements.txt` ✅
- `Procfile` or start command ✅
- Environment variables

### Add to requirements.txt

```bash
cd /root/context-search
cat >> requirements.txt << 'EOF'
python-multipart==0.0.6
EOF
```

### Environment Variables Needed

```
OPENAI_API_KEY=sk-...
API_KEYS=demo-key-123,another-key-456
```

## Step 2: Create Railway Project

1. Go to https://railway.app
2. Sign up with GitHub
3. New Project → Deploy from GitHub repo
4. Select `context-search` repo
5. Railway auto-detects Python + starts deploy

## Step 3: Set Environment Variables

In Railway dashboard:
- Variables tab
- Add: `OPENAI_API_KEY`
- Add: `API_KEYS`

## Step 4: Get Public URL

Railway provides: `yourapp-production.up.railway.app`

## Step 5: Test Deployed API

```bash
curl https://yourapp-production.up.railway.app/health
```

## Alternative: Manual Railway CLI Deploy

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Init project
cd /root/context-search
railway init

# Add env vars
railway variables set OPENAI_API_KEY=sk-...
railway variables set API_KEYS=demo-key-123

# Deploy
railway up
```

## Expected Cost

Railway pricing:
- $5/mo hobby plan
- Includes compute + 512MB RAM
- Perfect for MVP

---

**Ready to deploy?** Let me know and I'll help with each step.
