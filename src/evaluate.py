import json
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
import yaml


def load_params():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    return params["train"]


def load_data_and_model():
    # Dataset limpio
    df = pd.read_csv("data/processed/telco_clean.csv")

    # Modelo entrenado
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    return df, model


def prepare_data(df):
    df = df.copy()

    y = df["churn"]
    X = df.drop(columns=["churn"])

    # One-hot encoding igual que en train.py
    X = pd.get_dummies(X, drop_first=True)

    return X, y


def evaluate_model(X, y, model, params):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=params["test_size"],
        random_state=params["random_state"],
    )

    # Predicciones
    y_pred = model.predict(X_test)

    # Probabilidades para ROC
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)[:, 1]
    else:
        # Fallback raro, pero por las dudas
        y_proba = model.decision_function(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_proba),
    }

    # Curva ROC
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)

    return metrics, (fpr, tpr, thresholds)


def save_metrics_and_plot(metrics, roc_data):
    Path("reports").mkdir(exist_ok=True)

    # Guardar métricas extendidas
    with open("metrics_extended.json", "w") as f:
        json.dump(metrics, f, indent=4)

    # Guardar curva ROC
    fpr, tpr, _ = roc_data

    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC curve (AUC = {metrics['roc_auc']:.3f})")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Curva ROC - Modelo Telco Churn")
    plt.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig("reports/roc_curve.png")
    plt.close()


def main():
    print("Iniciando evaluación del modelo...")

    params = load_params()
    df, model = load_data_and_model()
    X, y = prepare_data(df)

    metrics, roc_data = evaluate_model(X, y, model, params)

    save_metrics_and_plot(metrics, roc_data)

    print("Evaluación completada.")
    print("Métricas extendidas:")
    print(json.dumps(metrics, indent=4))


if __name__ == "__main__":
    main()
