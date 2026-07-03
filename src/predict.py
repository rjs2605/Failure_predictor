import joblib
import pandas as pd

from src.logger import logger

model = joblib.load("models/model.pkl")
encoder = joblib.load("models/encoder.pkl")


def predict_failure(data):

    machine_type = encoder.transform([data.type])[0]

    sample = pd.DataFrame(
        [{
            "Type": machine_type,
            "Air temperature [K]": data.air_temperature,
            "Process temperature [K]": data.process_temperature,
            "Rotational speed [rpm]": data.rotational_speed,
            "Torque [Nm]": data.torque,
            "Tool wear [min]": data.tool_wear,
        }]
    )

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    logger.info(
        f"Prediction={prediction}, Probability={probability:.4f}"
    )

    return {
        "machine_failure": int(prediction),
        "prediction": "Failure" if prediction else "No Failure",
        "probability": round(float(probability), 4),
    }