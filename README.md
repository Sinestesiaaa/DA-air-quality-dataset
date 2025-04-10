# 🚴‍♂️ Bike Sharing Data Analysis & Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis dan memvisualisasikan data kualitas udara dari berbagai stasiun pemantauan di Tiongkok. Data mencakup berbagai parameter polusi seperti PM2.5, PM10, SO2, NO2, CO, dan O3 serta kondisi cuaca yang relevan. Analisis dilakukan menggunakan Python dengan pustaka seperti Pandas, Matplotlib, dan Seaborn, serta dibangun dashboard interaktif menggunakan **Streamlit**.

## 🎯 Tujuan Proyek

- 🔹 Melakukan pembersihan dan imputasi data polusi dan cuaca

- 🔹 Mengeksplorasi tren polusi berdasarkan waktu dan lokasi

- 🔹 Mengidentifikasi hubungan antara kondisi cuaca dan tingkat polusi

- 🔹 Menyediakan dashboard interaktif untuk eksplorasi data

## 🔍 Analisis yang Dilakukan

- ✅ **Rata-rata Polusi Berdasarkan Stasiun**

- ✅ **Tren Bulanan Polusi Tahun 2013–2017**

- ✅ **Korelasi antara Polutan dan Variabel Cuaca**

## 🛠 Teknologi yang Digunakan

- **Python** (Pandas, Matplotlib, Seaborn, Plotly)
- **Google Colab** untuk eksplorasi data
- **Streamlit** untuk pembuatan dashboard
- **Git & GitHub** untuk versi kontrol

## 🚀 Cara Menjalankan Proyek

### 1️⃣ Clone Repository
```
git clone https://github.com/username/air-quality-dataset.git

```
### 2️⃣ Buat Virtual Environment (Opsional, tetapi Disarankan)
Agar dependencies proyek tidak berbenturan dengan sistem, gunakan virtual environment.
```
pip install pipenv
pipenv install
pipenv shell
```
### 3️⃣ Install Dependensi
```
pip install -r requirements.txt
```
### 4️⃣ Jalankan Dashboard(Lokal)
```
streamlit run Dashboard/main.py
```