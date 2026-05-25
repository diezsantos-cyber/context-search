# Plan: PoC Vendible en 7-10 Días

**Objetivo:** Lanzar producto mínimo que alguien pague **ahora**, no en 4 semanas.

**Estrategia:** "Concierge MVP" - semi-manual al inicio, automatizar después.

---

## Week 1: PoC → Vendible (7 días)

### Día 1-2: API + Auth ✅ (ya empezamos)
- [x] PoC funcionando
- [ ] FastAPI REST endpoints:
  ```
  POST /index - sube repo zip, devuelve repo_id
  POST /search - query + repo_id → results JSON
  ```
- [ ] API key authentication (simple, no OAuth todavía)
- [ ] Deploy en Railway ($5/mes)

### Día 3-4: Landing Page + Stripe
- [ ] Landing page (Carrd o HTML simple):
  - **Problema:** "AI agents waste 1.4M tokens with grep"
  - **Solución:** "98% fewer tokens with semantic search"
  - **Demo:** Video 30seg mostrando búsqueda
  - **Pricing:** $49/mes - Beta Access
  - **CTA:** "Buy Now" → Stripe checkout
- [ ] Stripe integration:
  - 1 plan: Beta Access $49/mes
  - Webhook: payment success → email con API key

### Día 5-6: Documentación + Onboarding
- [ ] Docs mínimos (README):
  - Cómo usar la API
  - Ejemplo curl
  - Límites: 1 repo, 50K símbolos, 100 búsquedas/día
- [ ] Email template bienvenida:
  - API key
  - Link a docs
  - "Reply con tu repo GitHub y lo indexo manual"
- [ ] Script interno: indexar repo manual (yo lo corro)

### Día 7: Validación + Lanzamiento Soft
- [ ] Test end-to-end: compra → email → API funciona
- [ ] Outreach directo a 20 personas:
  - Commenters en Semble/Graphmind HN threads
  - r/ClaudeCode, r/Cursor posts
  - Mensaje: "Beta $49/mes, indexo tu repo manual, feedback = lifetime discount"
- [ ] **Meta:** 3-5 beta customers pagando

---

## Producto Mínimo Vendible (Day 7)

### Lo que SÍ tiene
✅ **API funcional** (index + search)
✅ **Pricing claro** ($49/mes beta)
✅ **Pago automático** (Stripe)
✅ **Docs básicos**
✅ **Soporte directo** (yo respondo emails)

### Lo que NO tiene (todavía)
❌ GitHub OAuth (manual: usuario me manda repo zip)
❌ Dashboard UI (solo API)
❌ Auto-indexing (manual: yo corro script)
❌ Multi-lenguaje (solo Python inicial)
❌ MCP server (viene después)

### Por qué funciona
- **Concierge approach:** Semi-manual al inicio es OKAY si el resultado es bueno
- **Early adopters:** No les importa fricción si resuelve su pain
- **Feedback directo:** Hablo con cada cliente, entiendo qué necesitan
- **Cash flow rápido:** $49 × 5 = $245/mes = valida demand ANTES de invertir 4 semanas

---

## Pricing Estrategia

### Beta Pricing (primeros 50 customers)
**$49/mes** - Beta Access
- 1 repo indexado (manual)
- 50K símbolos max
- 100 búsquedas/día
- API access
- Email support (24h response)
- **Lifetime lock-in:** precio no sube nunca para early adopters

### Why $49 not $99?
- Más fácil convencer beta testers
- Barrera psicológica baja
- Puedo decir "50% off" cuando lance pricing normal $99

### Incentivos para early adopters
- Precio locked ($49 forever)
- Influencia en roadmap
- Créditos en docs/testimonials
- Acceso anticipado a nuevas features

---

## GTM: Primeros 10 Customers (Día 7-14)

### Canal 1: Outreach Directo (20 mensajes/día)
**Target:** Personas que ya manifestaron el problema

1. **HN Commenters:**
   - Semble thread (434 pts) → 50+ commenters
   - Graphmind thread → 10+ commenters
   - Buscar "grep tokens" en HN → más threads

2. **Reddit:**
   - r/ClaudeCode → posts sobre context/tokens
   - r/Cursor → same
   - r/LocalLLaMA → agents

3. **LinkedIn:**
   - Buscar "AI agent developer"
   - CTO usando Cursor/Claude Code
   - Grupos: AI Dev Tools, LLM Engineering

**Mensaje template:**
```
Hey [name],

Saw your comment about [specific pain]. Built a tool that 
reduces agent token usage 98% vs grep using semantic search.

Beta: $49/mo, I index your repo manually, you get lifetime pricing.

Interested? [link]
```

### Canal 2: Show HN Post (Día 10)
**Title:** "Show HN: Context Search – 98% fewer tokens for AI agents (vs grep)"

**Post:**
```
Hi HN,

I built this after seeing Semble + Graphmind discussions about 
agent token waste. Semantic code search using embeddings.

Example: grep "payment" returns 5.9MB (1.4M tokens).
Context Search returns 1KB (257 tokens) - same result.

Currently Python only, manual indexing. Beta $49/mo.

[link to landing + demo]

Feedback welcome!
```

### Canal 3: Community Posts
- r/ClaudeCode, r/Cursor
- Dev.to, Hashnode blog post
- Twitter: thread con demo

**Target Week 2:** 10 paying customers = $490 MRR

---

## Automatización Roadmap (Post-Launch)

**Una vez tengo 10 customers pagando, automatizar:**

### Month 1 (después de 10 customers)
- GitHub OAuth (self-service indexing)
- Auto-reindex on push (webhook)
- Dashboard básico (ver repos, usage)

### Month 2
- Multi-lenguaje (JS, TS, Go)
- MCP server (Claude Code integration)
- Pricing tier $99 (unlimited)

### Month 3
- On-prem deployment ($499/mo enterprise)
- Team features (shared repos)
- Analytics (most searched symbols)

---

## Riesgos y Mitigaciones

### Riesgo 1: Nadie paga $49/mes
**Señal:** <3 customers en 2 semanas
**Mitigación:** Bajar a $29, ofrecer free trial 7 días
**Plan B:** Pivot a other use case (docs search, legal)

### Riesgo 2: Manual indexing no escala
**Señal:** >10 customers, 2h/día indexing
**Mitigación:** Priorizar auto-indexing feature
**Plan B:** Subir precio a $99, reducir customers

### Riesgo 3: Competencia lanza antes
**Señal:** Semble anuncia pricing, Graphmind saca SaaS
**Mitigación:** Speed to market (7 días vs su 4 semanas)
**Differentiation:** Pricing claro, mejor onboarding

### Riesgo 4: Churn alto (customers cancelan)
**Señal:** >50% churn Month 2
**Mitigación:** Exit interviews, feature requests
**Fix:** Agregar features que pidieron

---

## Métricas de Éxito

### Week 1 (Day 7)
- ✅ API deployed y funcional
- ✅ Landing page live
- ✅ Stripe checkout working
- ✅ 20 outreach messages sent
- 🎯 **Target:** 3 beta customers

### Week 2 (Day 14)
- ✅ Show HN posted
- ✅ 10 beta customers
- ✅ $490 MRR
- ✅ 3 testimonials/case studies
- 🎯 **Validation:** People ARE willing to pay

### Month 1 (Day 30)
- ✅ 25 customers
- ✅ $1,225 MRR
- ✅ GitHub OAuth live (self-service)
- ✅ <5% churn
- 🎯 **Decision:** Continue building vs pivot

---

## Decisiones Clave AHORA

### ¿Empezar construcción mañana?
- [ ] **SÍ** → continuar con plan Day 1-2 (FastAPI + deploy)
- [ ] **NO** → ¿qué bloquea?

### ¿Manual indexing está OK?
- [ ] **SÍ** → puedo dedicar 30min/día a indexar repos
- [ ] **NO** → necesito auto-indexing desde Day 1 (añade 3 días)

### ¿$49/mes es correcto?
- [ ] **SÍ** → usar este pricing
- [ ] **NO** → ¿cuánto? $___/mes

### ¿Quién hace landing page?
- [ ] **Yo (Pollux)** → HTML simple, deploy Vercel
- [ ] **Fenix** → diseño/copy
- [ ] **Contratar** → Fiverr $50-100

---

## Próximo Paso Inmediato

**Si decides GO:**

1. Confirmar decisiones arriba
2. Empiezo Day 1-2 (FastAPI + Railway deploy)
3. Objetivo: API funcional en Railway para mañana EOD
4. Luego Day 3-4 (landing + Stripe)

**¿Procedo?**
