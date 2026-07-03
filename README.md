🚀 Failure Predictor API

A Machine Learning-powered REST API built with FastAPI to predict whether an industrial machine is likely to fail based on its operating conditions.

---

📌 Overview

This project demonstrates a complete Machine Learning workflow:

- Data preprocessing
- Model training using Scikit-Learn
- Model serialization with Joblib
- REST API development using FastAPI
- Interactive API documentation (Swagger UI)
- Docker containerization
- Git & GitHub version control

---

🛠️ Tech Stack

- Python 3.12
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Uvicorn
- Docker
- Git
- uv (Python package manager)

---

📂 Project Structure

Failure_predictor/
│
├── data/
├── models/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   ├── schema.py
│   └── logger.py
│
├── app.py
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md

---

⚙️ Installation

Clone the repository:

git clone https://github.com/rjs2605/Failure_predictor.git

Move into the project:

cd Failure_predictor

Create the environment and install dependencies:

uv sync

---

▶️ Run the API

uv run uvicorn app:app --reload

API URL:

http://localhost:8000

Swagger Documentation:

http://localhost:8000/docs

---

🐳 Run with Docker

Build the Docker image:

docker build -t failure_predictor .

Run the container:

docker run -p 8000:8000 failure_predictor

---

📤 API Endpoint

POST "/predict"

Example Request

{
  "type": "L",
  "air_temperature": 298.1,
  "process_temperature": 308.6,
  "rotational_speed": 1551,
  "torque": 42.8,
  "tool_wear": 20
}

Example Response

{
  "machine_failure": 0,
  "prediction": "No Failure"
}

---

📈 Machine Learning Workflow

Dataset
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Serialization
   │
   ▼
FastAPI
   │
   ▼
REST API

---

📚 Features

- Machine failure prediction
- FastAPI REST API
- Interactive Swagger UI
- Docker support
- Clean project structure
- GitHub ready
- Easy deployment

---

🚀 Future Improvements

- Model monitoring
- MLflow integration
- CI/CD with GitHub Actions
- Kubernetes deployment
- Cloud deployment (Azure/AWS)
- Authentication and authorization
- Logging and monitoring

---

👨‍💻 Author

R. J. Suriya

GitHub: https://github.com/rjs2605

---

⭐ If you found this project useful, consider giving it a star on GitHub!
