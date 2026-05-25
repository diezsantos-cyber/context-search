#!/bin/bash
# Test API locally before deploying

API_KEY="demo-key-123"
BASE_URL="http://localhost:8000"

echo "Testing API..."

# Health check
echo -e "\n1. Health check:"
curl -s $BASE_URL/health | jq

# Create test zip
echo -e "\n2. Creating test repo zip..."
cd /tmp
mkdir test-repo
cp /root/context-search/example.py test-repo/
zip -q -r test-repo.zip test-repo/
cd -

# Index repo
echo -e "\n3. Indexing repo..."
REPO_RESPONSE=$(curl -s -X POST $BASE_URL/index \
  -H "X-API-Key: $API_KEY" \
  -F "file=@/tmp/test-repo.zip")
echo $REPO_RESPONSE | jq

REPO_ID=$(echo $REPO_RESPONSE | jq -r '.repo_id')
echo "Repo ID: $REPO_ID"

# Search
echo -e "\n4. Searching for 'payment processing'..."
curl -s -X POST $BASE_URL/search \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"payment processing\", \"repo_id\": \"$REPO_ID\"}" | jq

echo -e "\n5. Searching for 'user login'..."
curl -s -X POST $BASE_URL/search \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"user login\", \"repo_id\": \"$REPO_ID\"}" | jq

# List repos
echo -e "\n6. Listing repos..."
curl -s $BASE_URL/repos \
  -H "X-API-Key: $API_KEY" | jq

echo -e "\n✅ API test complete"
