import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")  
user = user_data_by_username()
st.set_page_config(page_title="DwTix - Profile")
user_db  = user_data_by_username()
username = st.session_state.username
user     = user_db[username]
st.title("👤 Profile")
st.divider()
# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password
st.text_input("Username", value=username, disabled=True)
st.text_input("Password", value=user["password"], disabled=True, type="password")
st.divider()
# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    if st.button("Logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username  = ""
        st.session_state.password  = ""
        st.switch_page("app.py")
        
with col2:
    if st.button("Ganti Data", type="secondary"):
        # simpan state bahwa form ganti password sedang dibuka
        st.session_state.show_ganti = True

if "show_ganti" not in st.session_state:
    st.session_state.show_ganti = False
 
if st.session_state.show_ganti:
    st.divider()
    st.subheader("🔒 Ganti Password")
 
    password_lama = st.text_input("Password lama", type="password", key="pw_lama")
    password_baru = st.text_input("Password baru", type="password", key="pw_baru")
 
    if st.button("Simpan", type="primary"):
 
        if password_lama != user["password"]:
            st.error("Password lama salah!")
 
        elif password_baru == password_lama:
            st.error("Password baru tidak boleh sama dengan password lama!")

        elif password_baru == "":
            st.error("Password baru tidak boleh kosong!")
 
        else:
            user_db[username]["password"] = password_baru
            st.session_state.password     = password_baru
            st.session_state.show_ganti   = False
            st.success("Password berhasil diubah!")
    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
