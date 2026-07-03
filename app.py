from fastapi import FastAPI, HTTPException

from src.predict import predict_failure
from src.schema import MachineInput

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Failure Predictor API Running"}


@app.post("/predict")
def predict(data: MachineInput):

    try:
        return predict_failure(data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )