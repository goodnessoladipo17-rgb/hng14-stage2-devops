#!/bin/bash
set -e

TIMEOUT=60
BASE_URL="http://localhost:3000"
API_URL="http://localhost:8000"

echo "Waiting for services..."
for i in $(seq 1 $TIMEOUT); do
  if curl -sf "$BASE_URL" > /dev/null 2>&1; then
    echo "Frontend is up!"
    break
  fi
  sleep 1
done

echo "Testing frontend..."
curl -f "$BASE_URL"

echo "Testing API..."
curl -f "$API_URL/docs"

echo "Testing job creation..."
JOB=$(curl -sf -X POST "$API_URL/jobs")
JOB_ID=$(echo $JOB | python3 -c "import sys,json; print(json.load(sys.stdin)['job_id'])")

echo "Testing job status..."
curl -f "$API_URL/jobs/$JOB_ID"

echo "All integration tests passed!"