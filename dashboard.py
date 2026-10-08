import streamlit as st
from user import user_data_by_username

st.set_page_config(page_title="DwTix - Dashboard")

# cek apakah sudah login -> JIKA BELUM ALIHKAN KE app.py
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")
# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
data = user_data_by_username()
# ambil role yang login dari data
username = st.session_state.username
role = data[username]["role"]
# role = ??

# JIKA YANG LOGIN PESERTA -> ALIHKAN KE PAGE EVENT
if role == "Peserta":
    st.switch_page("pages/event.py")

col_nav1, col_nav2 = st.columns([5, 1])
with col_nav2:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/profile.py")
 
st.title(f"Welcome, {role} 👋")
st.caption(f"Login sebagai: {username}")
st.divider()
 
# ADMIN — tampilkan seluruh data user
st.subheader("📋 Data Seluruh Pengguna")
 
# ubah dictionary ke format list of dict untuk tabel
tabel_data = []
for nama, info in data.items():
    tabel_data.append({
        "ID"      : info["id"],
        "Username": nama,
        "Role"    : info["role"],
        "Password": info["password"],
    })
 
st.table(tabel_data)
 
st.divider()
st.subheader("📊 Ringkasan")
 
# hitung jumlah per role
jumlah_peserta = sum(1 for u in data.values() if u["role"] == "Peserta")
jumlah_admin   = sum(1 for u in data.values() if u["role"] == "Admin")
 
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pengguna", len(data))
with col2:
    st.metric("Peserta", jumlah_peserta)
with col3:
    st.metric("Admin", jumlah_admin)
 

# JIKA YANG LOGIN ADMIN TAMPILKAN SELURUH DATA TERSERAH MAU BENTUKNYA APAPUN st.table, st.write boleh aja
