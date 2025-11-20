# automate_Aprilia-Melani.py
"""
===========================================================
Automate Preprocessing - Aprilia Melani
Kriteria: SKILLED (3 pts)
===========================================================

Cara menjalankan via CLI:

python automate_Aprilia-Melani.py \
    --input diabetes_raw/diabetes.csv \
    --output preprocessing/diabetes_preprocessing \
    --target diabetes

Output:
- X_train.csv
- X_test.csv
- y_train.csv
- y_test.csv
- scaler.joblib
- encoders.joblib

===========================================================
"""

import os
import argparse
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib



# =========================================================
# 1. LOAD DATASET
# =========================================================
def load_data(path):
    """Load dataset CSV."""
    return pd.read_csv(path)



# =========================================================
# 2. PREPROCESS FUNGSI UTAMA
# =========================================================
def preprocess_df(df):
    """Melakukan preprocessing sesuai eksperimen notebook."""

    # 1. Drop duplicates
    df.drop_duplicates(inplace=True)

    # 2. Outlier Handling - BMI (IQR Clipping)
    q1 = df['bmi'].quantile(0.25)
    q3 = df['bmi'].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df['bmi'] = df['bmi'].clip(lower, upper)

    # 3. Label Encoding untuk Kolom Kategori
    le_gender = LabelEncoder()
    le_smoking = LabelEncoder()

    df["gender"] = le_gender.fit_transform(df["gender"])
    df["smoking_history"] = le_smoking.fit_transform(df["smoking_history"])

    # 4. Scaling Fitur Numerik
    numerical_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    encoders = {
        "gender": le_gender,
        "smoking_history": le_smoking
    }

    return df, scaler, encoders



# =========================================================
# 3. PROSES PREPROCESSING → SAVE FILE
# =========================================================
def run_preprocessing(input_path, output_dir, target_col):
    """Main function untuk menjalankan preprocessing & menyimpan hasil."""

    os.makedirs(output_dir, exist_ok=True)

    print("🔄 Loading dataset...")
    df = load_data(input_path)

    print("🔄 Melakukan preprocessing...")
    df_clean, scaler, encoders = preprocess_df(df)

    # 5. Pisahkan fitur dan label
    X = df_clean.drop(columns=[target_col])
    y = df_clean[target_col]

    # 6. Train-test split (data siap dilatih)
    print("🔄 Melakukan train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 7. Simpan file CSV
    print("💾 Menyimpan file hasil preprocessing...")
    X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)

    # 8. Simpan scaler dan encoder untuk inference
    joblib.dump(scaler, os.path.join(output_dir, "scaler.joblib"))
    joblib.dump(encoders, os.path.join(output_dir, "encoders.joblib"))

    print("✅ Preprocessing selesai!")
    print("📁 Semua file disimpan ke folder:", output_dir)



# =========================================================
# 4. CLI UTAMA
# =========================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Preprocessing by Aprilia Melani")

    parser.add_argument("--input", required=True, help="Path file dataset CSV mentah")
    parser.add_argument("--output", required=True, help="Folder untuk output hasil preprocessing")
    parser.add_argument("--target", required=True, help="Nama kolom target (label)")

    args = parser.parse_args()

    run_preprocessing(args.input, args.output, args.target)
