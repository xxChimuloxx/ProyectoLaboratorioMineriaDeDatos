import pandas as pd
from pathlib import Path


def load_raw_data() -> pd.DataFrame:
    """
    Carga el dataset crudo desde data/raw.
    Soporta tanto .xlsx como .csv (por si se cambia el formato en el futuro).
    """
    raw_xlsx = Path("data/raw/telco_churn.xlsx")
    raw_csv = Path("data/raw/telco_churn.csv")

    if raw_xlsx.exists():
        print(f"Cargando datos desde: {raw_xlsx}")
        df = pd.read_excel(raw_xlsx)
    elif raw_csv.exists():
        print(f"Cargando datos desde: {raw_csv}")
        df = pd.read_csv(raw_csv)
    else:
        raise FileNotFoundError(
            "No se encontró ni data/raw/telco_churn.xlsx ni data/raw/telco_churn.csv"
        )

    return df


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica una limpieza básica sobre el dataset:
    - Normaliza nombres de columnas a minúsculas.
    - Convierte columnas numéricas a tipo numérico.
    - Elimina filas con valores faltantes críticos.
    - Elimina duplicados por customer_id.
    """
    print("Iniciando limpieza básica de datos...")

    # Normalizamos nombres de columnas
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]

    # Columnas que esperamos que sean numéricas
    numeric_cols = ["age", "tenure_months", "monthly_charges", "total_charges"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Aseguramos que churn sea numérico (0/1)
    if "churn" in df.columns:
        df["churn"] = pd.to_numeric(df["churn"], errors="coerce").astype("Int64")

    # Eliminamos filas con datos críticos faltantes
    critical_cols = ["customer_id", "age", "tenure_months", "monthly_charges", "total_charges", "churn"]
    existing_critical = [c for c in critical_cols if c in df.columns]

    before = len(df)
    df = df.dropna(subset=existing_critical)
    after = len(df)
    print(f"Filas antes de dropna: {before} | después: {after}")

    # Eliminamos duplicados por customer_id
    if "customer_id" in df.columns:
        before = len(df)
        df = df.drop_duplicates(subset=["customer_id"])
        after = len(df)
        print(f"Filas antes de eliminar duplicados: {before} | después: {after}")

    # Como paso final, nos aseguramos de que churn sea int estándar (no Int64 nullable)
    if "churn" in df.columns:
        df["churn"] = df["churn"].astype(int)

    print("Limpieza básica completa.")
    return df


def save_clean_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    Guarda el dataset limpio como CSV en la ruta indicada.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset limpio guardado en: {output_path}")


def main():
    print("Iniciando data_prep.py")

    # 1) Cargar datos crudos
    df_raw = load_raw_data()
    print(f"Dataset crudo: {df_raw.shape[0]} filas, {df_raw.shape[1]} columnas")

    # 2) Limpieza básica
    df_clean = basic_cleaning(df_raw)
    print(f"Dataset limpio: {df_clean.shape[0]} filas, {df_clean.shape[1]} columnas")

    # 3) Guardar resultado en data/processed
    output_path = Path("data/processed/telco_clean.csv")
    save_clean_data(df_clean, output_path)

    print("data_prep.py finalizado con éxito.")


if __name__ == "__main__":
    main()
