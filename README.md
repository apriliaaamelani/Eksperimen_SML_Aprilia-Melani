# 🩺 Eksperimen Machine Learning Prediksi Diabetes

## 📌 Gambaran Umum Proyek

Repository ini berisi eksperimen machine learning untuk prediksi diabetes menggunakan dataset klinis pasien yang bersumber dari Kaggle (100.000 catatan). Tujuan utamanya adalah membangun pipeline preprocessing data yang lengkap, mulai dari eksplorasi data mentah hingga menghasilkan dataset yang siap digunakan untuk pelatihan model.

Proyek ini mendemonstrasikan otomatisasi preprocessing menggunakan skrip Python berbasis Command Line Interface (CLI) serta otomatisasi CI/CD menggunakan GitHub Actions sehingga pipeline dapat dijalankan secara konsisten dan mudah direproduksi.

---

# 🎯 Tujuan Eksperimen

1. Melakukan eksplorasi dan memahami dataset diabetes.
2. Melakukan Exploratory Data Analysis (EDA).
3. Menerapkan teknik preprocessing data.
4. Membangun pipeline preprocessing otomatis menggunakan CLI.
5. Menghasilkan dataset yang siap digunakan untuk pelatihan model.
6. Mengotomatisasi proses preprocessing menggunakan GitHub Actions.

---

# 📂 Struktur Repository

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

# 📊 Informasi Dataset

**Platform** : Kaggle

**Link Dataset**

https://www.kaggle.com/datasets/mathchi/diabetes-data-set

**Jumlah Data**

- 100.000 baris
- 9 kolom

## Deskripsi Fitur

| Fitur | Tipe | Deskripsi |
|------|------|-----------|
| gender | Kategorikal | Jenis kelamin pasien |
| age | Float | Usia pasien |
| hypertension | Biner | Riwayat hipertensi |
| heart_disease | Biner | Riwayat penyakit jantung |
| smoking_history | Kategorikal | Riwayat merokok |
| bmi | Float | Body Mass Index |
| HbA1c_level | Float | Kadar Hemoglobin A1c |
| blood_glucose_level | Integer | Kadar glukosa darah |
| diabetes | Biner | Target (0 = Tidak Diabetes, 1 = Diabetes) |

## Statistik Dataset

| Metrik | Nilai |
|---------|-------|
| Total Data | 100.000 |
| Data Duplikat | 3.854 |
| Setelah Deduplikasi | 96.146 |
| Missing Value | 0 |
| Persentase Diabetes | ±8,5% |

---

# 🔬 Workflow Machine Learning

```text
Data Mentah (CSV)
        │
        ▼
 Exploratory Data Analysis
        │
        ▼
 Preprocessing
 ├── Menghapus Data Duplikat
 ├── Menangani Outlier BMI
 ├── Label Encoding
 ├── MinMax Scaling
 └── Train-Test Split
        │
        ▼
 Dataset Siap Training
```

---

# ⚙️ Tahapan Preprocessing

## 1. Menghapus Data Duplikat

Sebanyak **3.854** data duplikat dihapus agar kualitas dataset menjadi lebih baik.

---

## 2. Penanganan Outlier

Outlier pada fitur **BMI** ditangani menggunakan metode **IQR Clipping**.

```python
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

bmi = bmi.clip(lower_bound, upper_bound)
```

---

## 3. Label Encoding

Kolom kategorikal diubah menjadi numerik.

Kolom yang diencoding:

- gender
- smoking_history

---

## 4. Feature Scaling

Normalisasi menggunakan **MinMaxScaler** pada fitur:

- age
- bmi
- HbA1c_level
- blood_glucose_level

---

## 5. Train Test Split

Dataset dibagi menjadi:

- 80% Training
- 20% Testing

dengan

```python
random_state = 42
```

---

# 🤖 Menjalankan Script CLI

```bash
python preprocessing/automate_Aprilia-Melani.py \
    --input diabetes_raw/diabetes.csv \
    --output preprocessing/diabetes_preprocessing \
    --target diabetes
```

## Parameter

| Parameter | Keterangan |
|-----------|------------|
| --input | Path dataset mentah |
| --output | Folder hasil preprocessing |
| --target | Nama kolom target |

---

# 🔄 GitHub Actions

Workflow otomatis akan berjalan ketika:

- terdapat perubahan pada script preprocessing
- workflow dijalankan secara manual

Tahapan workflow:

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Menjalankan Script Preprocessing
5. Upload Artifact

---

# 📚 Library yang Digunakan

| Library | Fungsi |
|----------|--------|
| pandas | Manipulasi data |
| numpy | Komputasi numerik |
| scikit-learn | Preprocessing dan Machine Learning |
| joblib | Menyimpan scaler dan encoder |
| matplotlib | Visualisasi data |
| seaborn | Visualisasi statistik |
| argparse | Membaca parameter CLI |

---

# 🚀 Cara Menjalankan

## 1. Install Dependency

```bash
pip install pandas numpy scikit-learn joblib matplotlib seaborn
```

## 2. Jalankan Script

```bash
python preprocessing/automate_Aprilia-Melani.py \
    --input diabetes_raw/diabetes.csv \
    --output preprocessing/diabetes_preprocessing \
    --target diabetes
```

## 3. Jalankan Notebook

```bash
jupyter notebook preprocessing/Eksperimen_Aprilia-Melani.ipynb
```

---

# 👩‍💻 Pembuat

**Aprilia Melani**

Submission Dicoding — Belajar Machine Learning untuk Pemula 
---

# 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran sebagai bagian dari submission kursus Machine Learning.