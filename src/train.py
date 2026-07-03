import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.preprocess import preprocess_data


def main():

    df = pd.read_csv("data/ai4i2020.csv")

    X, y, encoder = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(f"Accuracy : {accuracy_score(y_test, predictions):.4f}")

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/model.pkl")
    joblib.dump(encoder, "models/encoder.pkl")

    print("Model Saved Successfully")


if __name__ == "__main__":
    main()