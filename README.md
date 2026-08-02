# 🐳 Docker Speedrun — Zerothon 2026

> From zero Docker knowledge to a live deployed app in one day.

![Docker](https://img.shields.io/badge/Docker-2563EB?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge)

---

## 🌍 Live Demo

👉 **[https://my-streamlit-app-44n5.onrender.com](https://my-streamlit-app-44n5.onrender.com)**

---

## 📖 About

This project was built during **Zerothon** — a 12-hour learn-a-thon — going from complete Docker beginner to deploying a containerized web app live on the internet.

**Built with:**
- 🐍 Python + Streamlit (web app)
- 🗄️ SQLite (built-in Python database)
- 🐳 Docker + Docker Compose (containerization)
- 🔄 GitHub Actions (CI/CD pipeline)
- ☁️ Render.com (cloud deployment)

---

## ✨ Features

- 📋 **Guestbook** — visitors can sign with their name and mood
- 📊 **Live mood chart** — bar chart updates as people sign
- 📈 **Visitor counter** — tracks total visits using SQLite
- 🔄 **Auto-deploy** — every push to main triggers a new Docker build and push via GitHub Actions

---

## 🗂️ Project Structure

```
docker-speedrun/
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker Compose config
├── .dockerignore           # Files excluded from Docker build
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions CI/CD pipeline
```

---

## 🚀 Run Locally with Docker

**Prerequisites:** Docker Desktop installed and running.

```bash
# Clone the repo
git clone https://github.com/Sathvika-g-29/docker-speedrun.git
cd docker-speedrun

# Build and run with Docker Compose
docker compose up --build

# Open in browser
http://localhost:8501
```

---

## 🐳 Pull from Docker Hub

```bash
docker pull sathvikaaa/my-streamlit-app:latest
docker run -p 8501:8501 sathvikaaa/my-streamlit-app:latest
```

👉 Docker Hub: [hub.docker.com/r/sathvikaaa/my-streamlit-app](https://hub.docker.com/r/sathvikaaa/my-streamlit-app)

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch automatically:

1. ✅ Checks out the latest code
2. 🔐 Logs into Docker Hub using GitHub Secrets
3. 🏗️ Builds the Docker image
4. 📤 Pushes `:latest` tag to Docker Hub

**GitHub Secrets required:**
| Secret | Value |
|--------|-------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token |

---

## 🏗️ Multi-Stage Docker Build

This project uses a multi-stage Dockerfile to keep the image slim:

| Stage | Purpose | Result |
|-------|---------|--------|
| `builder` | Install all Python packages | Heavy (has pip, build tools) |
| `runtime` | Copy only installed packages | **Light — this is the final image** |

**Size comparison:**
- Single-stage build: **1.03 GB**
- Multi-stage build: **783 MB**
- Savings: **250 MB** 🎉

---

## 📚 What I Learned

| Topic | Details |
|-------|---------|
| Docker basics | Images, containers, Dockerfile, registry |
| Dockerfile | FROM, WORKDIR, COPY, RUN, EXPOSE, CMD |
| Layer caching | Copy requirements before code for faster builds |
| Docker Compose | Multi-service orchestration with one command |
| Docker Hub | Tagging, pushing, pulling images |
| Deployment | Render.com free tier with Docker image |
| CI/CD | GitHub Actions workflow for auto-deploy |
| Optimization | Multi-stage builds + .dockerignore |

---

## ⚡ Quick Command Reference

```bash
# Build
docker build -t my-streamlit-app .

# Run
docker run -p 8501:8501 my-streamlit-app

# Compose
docker compose up -d          # start in background
docker compose down           # stop everything
docker compose logs -f        # live logs

# Docker Hub
docker tag my-streamlit-app sathvikaaa/my-streamlit-app:v1
docker push sathvikaaa/my-streamlit-app:v1
```

---

## 👩‍💻 Author

**Sathvika** — built at Zerothon, August 1, 2026

> *"From `docker run hello-world` to a live deployed app in 12 hours."*

---

⭐ If this helped you learn Docker, give it a star!
