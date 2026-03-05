# Student Exam Score Prediction API

This project is a machine learning API that predicts a student's exam score based on different performance factors such as study time, sleep hours, attendance, previous scores, and other related features.

The model is trained using CatBoost (with a scikit-learn preprocessing pipeline) and exposed through a FastAPI application. The project is containerized with Docker for easier deployment.

---

## What this project does

- Trains a regression model to predict exam scores
- Uses preprocessing with scikit-learn
- Serves predictions through a FastAPI REST API
- Can be run locally or inside a Docker container

---

## Tech Stack

- Python
- scikit-learn
- CatBoost
- FastAPI
- Uvicorn
- Docker

---

## How to run locally

1. Install dependencies:

```bash
pip install -r reqs.txt


uvicorn app:app --reload

docker build -t student-score-api 

docker run -p 8000:8000 student-score-api