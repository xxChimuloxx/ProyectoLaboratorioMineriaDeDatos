import json
import pickle
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import yaml


def load_params():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    return params["train"]


def load_clean_data():
    df = pd.read_csv("data/processed/telco_clean.csv")
    return df


def prepare_data(df):
    # 1) Variables numéricas y categóricas (dummy encoding)
    df = df.copy()

    # Variable objetivo
    y = df["churn"]

    # Features: todas menos churn
    X = df.drop(columns=["churn"])

    # One-hot encoding para variables categóricas
    X = pd.get_dummies(X, drop_first=True)

    return X, y


def train_model(X, y, params):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=params["test_size"],
        random_state=params["random_state"]
    )

    model = LogisticRegression(
        max_iter=params["max_iter"],
        solver=params["solver"],
        C=params["C"]
    )

    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    metrics = {
        "accuracy": acc,
        "f1_score": f1
    }

    return model, metrics


def save_outputs(model, metrics):
    # Guardar modelo
    Path("models").mkdir(exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Guardar métricas
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)


def main():
    print("Entrenando modelo...")
    print("Entrenamiento iniciado desde rama experimental...")

    params = load_params()
    df = load_clean_data()
    X, y = prepare_data(df)

    model, metrics = train_model(X, y, params)

    save_outputs(model, metrics)

    print("Modelo entrenado con éxito.")
    print("Métricas:")
    print(metrics)


if __name__ == "__main__":
    main()
