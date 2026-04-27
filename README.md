Bike Sharing Analysis Dashboard 

A. Deskripsi
Proyek ini bertujuan untuk menganalisis tren penyewaan sepeda berdasarkan faktor cuaca dan waktu. Analisis dilakukan menggunakan Python dan divisualisasikan melalui dashboard interaktif Streamlit.

B. Struktur Folder
- `dashboard/`: Berisi file dashboard (`dashboard.py`) dan data yang sudah diolah (`main_data.csv`).
- `data/`: Berisi dataset mentah (`day.csv` dan `hour.csv`).
- `notebook.ipynb`: Dokumentasi lengkap proses analisis data.

C. Cara Menjalankan Dashboard
1. Instal library:
   ```bash
   pip install pandas matplotlib seaborn streamlit
2. Jalankan:
streamlit run dashboard/dashboard.py