# 🩺 Diabetes Prediction Machine Learning Experiment

## 📌 Project Overview

This repository contains a machine learning experiment focused on diabetes prediction using a clinical patient dataset sourced from Kaggle (100,000 records). The primary objective is to build a complete data preprocessing pipeline, starting from raw data exploration to generating model-ready training and testing datasets.

The project demonstrates automated preprocessing through a Python Command Line Interface (CLI) script and CI/CD automation using GitHub Actions, ensuring the preprocessing workflow is consistent, reproducible, and easy to execute.

---

# 🎯 Objectives

1. Explore and understand the diabetes dataset.
2. Perform Exploratory Data Analysis (EDA).
3. Apply data preprocessing techniques.
4. Build an automated preprocessing pipeline using CLI.
5. Produce model-ready datasets for machine learning.
6. Implement CI/CD automation with GitHub Actions.

---

# 📂 Repository Structure

```text
Eksperimen_SML_Aprilia-Melani/
│
├── .github/
│   └── workflows/
│       └── preprocessing.yml
│
├── diabetes_raw/
│   └── diabetes.csv
│
├── preprocessing/
│   ├── automate_Aprilia-Melani.py
│   ├── Eksperimen_Aprilia-Melani.ipynb
│   ├── diabetes_preprocessing.csv
│   └── diabetes_preprocessing/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── scaler.joblib
│       └── encoders.joblib
│
├── README.md
└── README_ENG.md
```

---

# 📊 Dataset Information

**Platform**

Kaggle

**Dataset Link**

https://www.kaggle.com/datasets/mathchi/diabetes-data-set

**Dataset Size**

- 100,000 records
- 9 columns

## Features

| Feature | Type | Description |
|---------|------|-------------|
| gender | Categorical | Patient gender |
| age | Float | Patient age |
| hypertension | Binary | Hypertension status |
| heart_disease | Binary | Heart disease status |
| smoking_history | Categorical | Smoking history |
| bmi | Float | Body Mass Index |
| HbA1c_level | Float | Hemoglobin A1c level |
| blood_glucose_level | Integer | Blood glucose level |
| diabetes | Binary | Target variable (0 = No Diabetes, 1 = Diabetes) |

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Records | 100,000 |
| Duplicate Records | 3,854 |
| Records After Deduplication | 96,146 |
| Missing Values | 0 |
| Diabetes Positive Rate | Approximately 8.5% |

---

# 🔬 Machine Learning Workflow

```text
Raw Dataset (CSV)
        │
        ▼
 Exploratory Data Analysis
        │
        ▼
 Data Preprocessing
 ├── Remove Duplicate Records
 ├── Handle BMI Outliers
 ├── Label Encoding
 ├── MinMax Feature Scaling
 └── Train-Test Split
        │
        ▼
 Model-Ready Dataset
```

---

# ⚙️ Preprocessing Pipeline

## 1. Remove Duplicate Records

A total of **3,854** duplicate records are removed to improve dataset quality.

---

## 2. Outlier Handling

BMI outliers are handled using the **IQR Clipping** method.

```python
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

bmi = bmi.clip(lower_bound, upper_bound)
```

---

## 3. Label Encoding

Categorical features are converted into numerical values.

Encoded columns:

- gender
- smoking_history

---

## 4. Feature Scaling

Numerical features are normalized using **MinMaxScaler**.

Scaled features:

- age
- bmi
- HbA1c_level
- blood_glucose_level

---

## 5. Train-Test Split

The dataset is divided into:

- 80% Training
- 20% Testing

using

```python
random_state = 42
```

---

# 🤖 CLI Usage

```bash
python preprocessing/automate_Aprilia-Melani.py \
    --input diabetes_raw/diabetes.csv \
    --output preprocessing/diabetes_preprocessing \
    --target diabetes
```

## Arguments

| Argument | Description |
|----------|-------------|
| --input | Path to the raw dataset |
| --output | Output directory for preprocessed files |
| --target | Target column name |

---

# 🔄 GitHub Actions

The workflow automatically runs when:

- changes are pushed to the preprocessing script
- triggered manually using **workflow_dispatch**

Workflow steps:

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Run Preprocessing Script
5. Upload Generated Artifacts

---

# 📚 Libraries Used

| Library | Purpose |
|----------|---------|
| pandas | Data manipulation and analysis |
| numpy | Numerical computing |
| scikit-learn | Data preprocessing and machine learning utilities |
| joblib | Save and load scaler & encoder objects |
| matplotlib | Data visualization |
| seaborn | Statistical visualization |
| argparse | Command-line argument parsing |

---

# 🚀 Quick Start

## 1. Install Dependencies

```bash
pip install pandas numpy scikit-learn joblib matplotlib seaborn
```

## 2. Run the Preprocessing Script

```bash
python preprocessing/automate_Aprilia-Melani.py \
    --input diabetes_raw/diabetes.csv \
    --output preprocessing/diabetes_preprocessing \
    --target diabetes
```

## 3. Open the EDA Notebook

```bash
jupyter notebook preprocessing/Eksperimen_Aprilia-Melani.ipynb
```

---

# 👩‍💻 Author

**Aprilia Melani**

Submission: Dicoding — *Belajar Machine Learning untuk Pemula* 

---

# 📄 License

This project was created for educational purposes as part of a Machine Learning course submission.