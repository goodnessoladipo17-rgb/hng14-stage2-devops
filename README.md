# HNG Stage 2 - DevOps

A multi-service job processing application with CI/CD pipeline.

## Services
- **API** - FastAPI backend (port 8000)
- **Worker** - Background job processor
- **Frontend** - Node.js frontend (port 3000)
- **Redis** - Message queue

## Prerequisites
- Docker Desktop
- Docker Compose

## Run Locally
git clone https://github.com/goodnessoladipo17-rgb/hng14-stage2-devops
cd hng14-stage2-devops
docker compose up

Then open http://localhost:3000

## CI/CD
GitHub Actions pipeline runs on every push to main:
- Builds all Docker images
- Starts all services
- Tests frontend and API endpoints
- Stops services