# Deploy Alternatives - Railway Free Plan Agotado

## Opción 1: Render (Recomendado - FREE)

**Ventajas:**
- Free tier generoso (750 horas/mes)
- Deploy desde GitHub automático
- Más fácil que Railway
- No requiere tarjeta de crédito

### Pasos:

1. Ve a https://render.com
2. Sign up con GitHub
3. "New" → "Web Service"
4. Conecta repo `context-search`
5. Settings:
   - Name: `context-search`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
6. Environment Variables:
   - `OPENAI_API_KEY` = tu key
   - `API_KEYS` = `beta-key-001,beta-key-002,beta-key-003`
7. Click "Create Web Service"
8. Espera 2-3 min
9. URL: `https://context-search.onrender.com`

---

## Opción 2: Fly.io (FREE - más técnico)

**Ventajas:**
- Free tier: 3 VMs pequeñas
- Más control
- CLI potente

### Pasos:

```bash
# Instalar CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Deploy
cd /root/context-search
fly launch
# Responde:
# - App name: context-search
# - Region: closest to you
# - PostgreSQL: No
# - Redis: No
# - Deploy now: Yes

# Agregar secrets
fly secrets set OPENAI_API_KEY=sk-...
fly secrets set API_KEYS=beta-key-001,beta-key-002,beta-key-003

# URL: https://context-search.fly.dev
```

---

## Opción 3: Vercel (FREE - solo si agregamos serverless)

Vercel normalmente es para frontend, pero puede hacer APIs con serverless functions.

**Requiere:** Convertir FastAPI a serverless (30 min extra trabajo)

---

## Opción 4: Heroku ($7/mo - PAID pero confiable)

**Ventajas:**
- Muy estable
- Usado por millones
- $7/mo Eco Dynos

### Pasos:

1. https://heroku.com → Sign up
2. Install Heroku CLI: `curl https://cli-assets.heroku.com/install.sh | sh`
3. Deploy:

```bash
cd /root/context-search
heroku login
heroku create context-search
git push heroku main
heroku config:set OPENAI_API_KEY=sk-...
heroku config:set API_KEYS=beta-key-001,beta-key-002,beta-key-003
```

URL: `https://context-search.herokuapp.com`

---

## Opción 5: PythonAnywhere (FREE limitado)

**Ventajas:**
- Específico para Python
- Free tier existe
- Fácil

**Desventajas:**
- Free tier tiene límites estrictos
- Solo 1 app

---

## 🎯 MI RECOMENDACIÓN: **Render**

**Por qué:**
- ✅ 100% gratis (750h/mes = suficiente)
- ✅ Más fácil que Railway
- ✅ Deploy automático desde GitHub
- ✅ No requiere tarjeta
- ✅ Usado por muchas startups

**El código ya está listo, solo necesitas:**
1. Crear cuenta Render
2. Conectar GitHub
3. Agregar variables
4. Deploy

**Tiempo estimado: 10 minutos**

---

## Siguiente Paso

¿Quieres que te guíe con **Render**? Es la opción más rápida.
