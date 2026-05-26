# Render Deploy - Paso a Paso

## Estás en "My Workspace" - Ahora sigue:

### Paso 1: Crear Web Service (2 min)

1. Click botón azul **"New +"** (arriba derecha)
2. Selecciona **"Web Service"**
3. En la siguiente pantalla:
   - Verás opción "Connect a repository"
   - Click **"Connect account"** o **"Configure account"**
4. Autoriza Render en GitHub
5. Busca y selecciona: `diezsantos-cyber/context-search`
6. Click **"Connect"**

---

### Paso 2: Configurar el Servicio (3 min)

Render te muestra un formulario, llena:

**Basics:**
- **Name:** `context-search` (o lo que quieras)
- **Region:** Elige el más cercano (e.g., Oregon USA)
- **Branch:** `main`
- **Root Directory:** (déjalo vacío)

**Build & Deploy:**
- **Runtime:** `Python 3`
- **Build Command:** 
  ```
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```
  uvicorn api:app --host 0.0.0.0 --port $PORT
  ```

**Instance:**
- **Instance Type:** Selecciona **"Free"** ($0/mo)

---

### Paso 3: Environment Variables (2 min)

Scroll down hasta **"Environment Variables"**

Click **"Add Environment Variable"** 3 veces:

**Variable 1:**
- Key: `OPENAI_API_KEY`
- Value: `sk-proj-...` (tu OpenAI key)

**Variable 2:**
- Key: `API_KEYS`
- Value: `beta-key-001,beta-key-002,beta-key-003`

**Variable 3:**
- Key: `PORT`
- Value: `10000`

---

### Paso 4: Deploy! (1 min)

1. Scroll hasta abajo
2. Click botón azul **"Create Web Service"**
3. Render empezará a buildear

---

### Paso 5: Esperar Deploy (2-3 min)

Verás pantalla con logs en tiempo real:

```
==> Cloning from https://github.com/diezsantos-cyber/context-search...
==> Installing dependencies from requirements.txt
==> Starting service with: uvicorn api:app...
==> Your service is live!
```

Cuando veas **"Your service is live"** → ✅ LISTO

---

### Paso 6: Copiar URL

Arriba verás algo como:
```
https://context-search-XXXX.onrender.com
```

**COPIA ESA URL** - es tu API pública

---

### Paso 7: Probar API

Abre nueva terminal y prueba:

```bash
curl https://context-search-XXXX.onrender.com/health
```

Debería devolver:
```json
{"status":"healthy"}
```

✅ **API funcionando!**

---

## Siguiente Paso

Una vez que la API esté live:
1. Guarda la URL
2. Desplegamos landing page en Vercel
3. Actualizamos docs con la URL real
4. ¡Listo para primeros clientes!

---

**¿Dónde estás ahora? ¿Ya hiciste click en "New +"?**
