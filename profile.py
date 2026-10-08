import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
    
user = user_data_by_username()

# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password

# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    pass
        
with col2:
    pass
    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
