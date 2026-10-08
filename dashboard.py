import streamlit as st
from user import user_data_by_username

st.set_page_config(page_title="DwTix - Dashboard")

# cek apakah sudah login -> JIKA BELUM ALIHKAN KE app.py
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.switch_page("login.py")
# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
data = user_data_by_username()
# ambil role yang login dari data
# role = ??
username_input = st.text_input("username")
password_input = st.text_input("password")

if st.button("Login Dashboard"):
    for nama, data in data.items():
        role = data["role"]
        if username_input == nama and password_input == data["password"]:
            if data["role"] == "Admin":
                st.write("Koniciwa")
            elif data["role"] == "Peserta":
                st.session_state['logged_in'] = True
                st.switch_page("app.py")



# JIKA YANG LOGIN PESERTA -> ALIHKAN KE PAGE EVENT

st.title(f"Welcome, {role} 👋")

# JIKA YANG LOGIN ADMIN TAMPILKAN SELURUH DATA TERSERAH MAU BENTUKNYA APAPUN st.table, st.write boleh aja