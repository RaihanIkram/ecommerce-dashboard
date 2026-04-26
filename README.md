# E-Commerce Customer Dashboard

Dashboard ini digunakan untuk menganalisis data e-commerce dengan fokus pada:

* Distribusi segmentasi pelanggan (RFM)
* Kontribusi revenue berdasarkan kategori produk

Dashboard membantu memahami perilaku pelanggan serta kategori produk yang paling berkontribusi terhadap pendapatan.


## Struktur Proyek

submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── notebook.ipynb
├── requirements.txt
└── README.md


##  Setup Environment

Gunakan virtual environment untuk menghindari konflik library.

### 1. Membuat Virtual Environment

```bash
python -m venv venv
```

### 2. Aktivasi Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```


##  Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Menjalankan Dashboard

```bash
streamlit run dashboard/dashboard.py
```

Akses melalui browser:
http://localhost:8501

---

##  Fitur Dashboard

* Filter berdasarkan segment pelanggan (Low, Mid, High)
* Visualisasi distribusi pelanggan
* Top 10 kategori produk berdasarkan revenue
* Tampilan interaktif dan mudah dipahami

---

##  Catatan

Pastikan file `main_data.csv` berada di dalam folder `dashboard/`.
