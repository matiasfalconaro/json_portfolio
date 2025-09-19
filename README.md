# JSON Portfolio
Hey! Welcome to my portfolio, and thank you for your interest!

## Overview
![Architecture](https://github.com/matiasfalconaro/json_portfolio/raw/main/docs/architecture.svg)

# Infrastructure
## Build (From an EC2 instance, using [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit), AWS)
```bash
sudo su ec2-user
cd ~/reflex_ec2_toolkit
git clone https://github.com/matiasfalconaro/ec2-reflex-toolkit.git
```

For more information, visit [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit).

# CI/CD
## Trigger pipeline (From a tag in main, locally)
```bash
git tag <vx.y.z>
git push origin <vx.y.z>
```

## Deploy (From an EC2 using [Reflex-EC2-Toolkit](https://github.com/matiasfalconaro/ec2-reflex-toolkit), AWS)
```bash
sudo ./run.sh --only deploy
```

# Unit tests
Version-dependent tests use version.txt.

## Run all, a test script, or a specific test:
```bash
pytest -v
pytest -v tests/test_components.py
pytest -v tests/test_components.py::test_navbar_returns_component
```
