# ⚙️ Microservices Demo — Users & Orders Services

A fully containerized microservices project built with **FastAPI**, **Docker**, and **GitHub Actions CI**.  
This project demonstrates service-to-service communication, clean API design, modular architecture, and automated testing.

---

# CI Status

![CI](https://github.com/Lyynn777/microservices-demo/actions/workflows/ci.yml/badge.svg)

This project has **automated CI** that:

- Builds both microservice Docker images  
- Starts services using Docker Compose  
- Installs dependencies  
- Runs unit tests  
- Shuts down containers  

You can view the full pipeline in the **Actions** tab.

---

# Features

### 🟦 Users Service
- Create new users
- Retrieve a user
- Update status and credit
- Simple in-memory storage
- Auto-generated API docs via FastAPI

### 🟩 Orders Service
- Create orders
- Validates user via Users service
- Calculates total price
- Ensures user is active + has enough credit
- Mocked external service inside tests

### 🔧 DevOps
- Fully Dockerized microservices
- Docker Compose orchestration
- GitHub Actions CI/CD
- Unit tests with pytest
- Modular Python package structure

---

# Run With Docker (Recommended)

This starts **both** services using Docker Compose.

```bash
docker compose up --build
```
After build completes:

Service	URL
Users Service	http://localhost:8001/docs
Orders Service	http://localhost:8002/docs

Unit Tests
Unit tests run automatically inside GitHub Actions.

To run locally (optional):
```
cd orders
pytest -vv
```
Tests include:
Success cases
Insufficient credit
Inactive user
User not found
Mocked Users service

---
# Technologies Used
- Python 3.11
- FastAPI
- httpx
- Pydantic
- Docker
- Docker Compose
- Pytest
- GitHub Actions CI
---

# Future Enhancements
- PostgreSQL instead of in-memory DB
- Service discovery / API Gateway
- Redis caching
- Monitoring with Prometheus + Grafana
- Deployment to Railway / Render


