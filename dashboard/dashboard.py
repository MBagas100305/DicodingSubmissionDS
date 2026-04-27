import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page title
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Header
st.title("Bike Sharing Analysis Dashboard")

# Load Data
@st.cache_data
def load_data():
    # Mengambil jalur folder tempat file dashboard.py berada
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Menggabungkan jalur folder tadi dengan nama file
    # Pastikan namanya "main_data.csv" atau "all_data.csv" (sesuaikan dengan isi foldermu!)
    file_path = os.path.join(current_dir, "all_data.csv")
    
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# Sidebar untuk Filter
with st.sidebar:
    st.header("Filter Data")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=main_df['dteday'].min(),
        max_value=main_df['dteday'].max(),
        value=[main_df['dteday'].min(), main_df['dteday'].max()]
    )

# Filter Data
filtered_df = main_df[(main_df['dteday'] >= str(start_date)) & 
                       (main_df['dteday'] <= str(end_date))]

# Layout Dashboard Utama
col1, col2 = st.columns(2)

with col1:
    st.subheader("Penyewaan Berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=filtered_df, palette='viridis', ax=ax)
    ax.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan/Salju)")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

with col2:
    st.subheader("Korelasi Suhu vs Penyewaan")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(x='temp', y='cnt', data=filtered_df, scatter_kws={'alpha':0.3}, line_kws={'color':'red'}, ax=ax)
    ax.set_xlabel("Suhu (Normalized)")
    ax.set_ylabel("Total Penyewaan")
    st.pyplot(fig)

# --- BAGIAN INSIGHT ---
st.divider()
st.subheader("Key Insights 💡")

with st.expander("Lihat Detail Analisis"):
    st.markdown(f"""
    - **Pengaruh Cuaca:** Berdasarkan data dari **{start_date}** hingga **{end_date}**, terlihat bahwa jumlah penyewaan sepeda mencapai puncaknya pada kondisi cuaca **Cerah (1)**. Sebaliknya, penurunan drastis terjadi saat cuaca **Hujan/Salju (3)**. Hal ini menunjukkan bahwa kenyamanan dan keamanan berkendara adalah prioritas pengguna.
    
    - **Hubungan Suhu:** Grafik regresi di sebelah kanan menunjukkan adanya **korelasi positif yang kuat** antara suhu (`temp`) dengan jumlah penyewa (`cnt`). Semakin hangat suhu (dalam batas wajar), semakin tinggi minat masyarakat untuk menggunakan layanan bike-sharing.
    
    - **Rekomendasi Bisnis:** 1. Pastikan jumlah sepeda tersedia maksimal saat prakiraan cuaca cerah dan suhu hangat.
        2. Berikan promo khusus atau perlengkapan tambahan (seperti mantel gratis) saat cuaca mendung/lembab untuk menjaga kestabilan penyewaan.
    """)

st.caption('Copyright (c) Muhammad Bagas Althaafah - 2026')
