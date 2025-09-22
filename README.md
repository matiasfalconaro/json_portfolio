# JSON Portfolio
Hey! Welcome to my portfolio, and thank you for your interest!

## Overview
This project is a personal portfolio built with [Reflex](https://reflex.dev) as the frontend/backend framework
and **MongoDB** as the persistent datastore.  
It evolved from a static JSON-based portfolio to a Dockerized microservice architecture.

![Architecture](https://github.com/matiasfalconaro/json_portfolio/raw/main/docs/architecture.svg)

# Infrastructure
## Build (From an EC2 instance, using [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit), AWS)
```bash
sudo su ec2-user
cd ~
git clone https://github.com/matiasfalconaro/ec2-reflex-toolkit.git
```

For more information, visit [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit).

# Getting Started

## Requirements
- Docker & Docker Compose
- Python 3.10+ (for local dev/test)

## Run with Docker Compose
```bash
docker-compose up --build
```

# Data Import
On first startup, import your resume.json into MongoDB:
```bash
python database/bulk_import.py
```
This will create collections and indexes if they don’t exist.

# CI/CD
## Trigger pipeline (From a tag in main, locally)
```bash
git tag <vx.y.z>
git push origin --tags
```

## Deploy (From an EC2 using [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit), AWS)
```bash
sudo ./run.sh --only deploy
```

# Unit tests
Version-dependent tests use `version.txt`.

## Run all, a test script, or a specific test:
```bash
pytest -v
pytest -v tests/test_components.py
pytest -v tests/test_components.py::test_navbar_returns_component
```

# BDD Tests
Gherkin-style tests using pytest-bdd for behavior specification and acceptance criteria.

## Run all BDD tests:
```bash
pytest -v tests/steps/
```

## Run specific BDD test categories:
```bash
pytest -v tests/steps/test_components_steps.py
```

## Run specific test functions:
```bash
pytest -v tests/test_components.py::test_navbar_returns_component
```

## Run Complete Test Suite
```bash
pytest -v tests/ tests/steps/
```