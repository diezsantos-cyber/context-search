# Context Search - Efficient Code Search for AI Agents

**Status:** Building MVP (Day 1)

## What This Does

Indexes code repositories and provides semantic search that uses **98% fewer tokens** than grep.

Instead of:
```bash
grep "payment processing"  # Returns 5.9MB (1.4M tokens)
```

You get:
```python
search("payment processing")  # Returns 1KB (257 tokens) - targeted results
```

## Current Progress

- [x] Project structure
- [x] Simple symbol parser (Python)
- [x] OpenAI embeddings integration
- [x] Semantic search (cosine similarity)
- [ ] PoC test
- [ ] Tree-sitter integration (proper AST)
- [ ] FastAPI REST API
- [ ] GitHub integration
- [ ] MCP server
- [ ] Multi-language support (JS, TS, Go)

## Quick Test (Once venv ready)

```bash
# 1. Add your OpenAI API key
cp .env.example .env
# Edit .env and add your key

# 2. Run PoC
source venv/bin/activate
python poc.py example.py "payment processing"
```

Expected output:
```
📄 Parsing example.py...
✅ Found 8 symbols
🧠 Generating embeddings...
🔍 Searching for: 'payment processing'

📊 Top 5 results:

1. class 'PaymentProcessor' (line 6) - similarity: 0.892
2. method 'process_credit_card' (line 9) - similarity: 0.856
3. method '_charge' (line 20) - similarity: 0.774
...
```

## Next Steps

1. Test PoC with real repo
2. Measure token savings (grep vs semantic)
3. Add FastAPI endpoints
4. Deploy MVP to Railway

---

**Target:** Week 1 complete by 2026-06-01
