# FIXES.md

## Bug Fixes Documentation

### Fix 1
- **File:** api/main.py
- **Line:** 9
- **Problem:** Redis host hardcoded as localhost — won't work in Docker
- **Fix:** Changed to use environment variable os.getenv("REDIS_HOST", "redis")

### Fix 2
- **File:** worker/worker.py
- **Line:** 6
- **Problem:** Redis host hardcoded as localhost — won't work in Docker
- **Fix:** Changed to use environment variable os.getenv("REDIS_HOST", "redis")

### Fix 3
- **File:** worker/worker.py
- **Line:** 4
- **Problem:** signal imported but never used, no graceful shutdown handling
- **Fix:** Added signal handlers for SIGTERM and SIGINT

### Fix 4
- **File:** frontend/app.js
- **Line:** 6
- **Problem:** API URL hardcoded as http://localhost:8000, won't work in Docker
- **Fix:** Changed to use environment variable process.env.API_URL

### Fix 5
- **File:** api/.env
- **Line:** 1-2
- **Problem:** Real credentials committed to GitHub in .env file
- **Fix:** Deleted .env file, added .env to .gitignore, created .env.example

### Fix 6
- **File:** api/requirements.txt
- **Line:** 1-3
- **Problem:** No version numbers pinned, could install breaking versions
- **Fix:** Pinned exact versions for fastapi, uvicorn, and redis

### Fix 7
- **File:** worker/requirements.txt
- **Line:** 1
- **Problem:** No version number pinned for redis
- **Fix:** Pinned exact version redis==5.0.1

### Fix 8
- **File:** frontend/package.json
- **Line:** 9-10
- **Problem:** Dependencies use ^ which allows unpredictable version updates
- **Fix:** Removed ^ to pin exact versions

### Fix 9
- **File:** frontend/views/index.html
- **Line:** 32-34
- **Problem:** Polling never stops if job status is failed or error
- **Fix:** Updated condition to stop polling on both completed and failed statuses