import streamlit as st
from user import user_data_by_username

# set tab title -> https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation silahkan kalau mau baca karena gabut awoaowawo
st.set_page_config(page_title="DwTix - Login")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""
# deklarasi sesi username, password, dan status login


# kalau misal ada error itu gara gara versi streamlit minimal 1.52.0 ya
# silahkan up pakai pip install --upgrade streamlit
# page header
st.header("Selamat datang kembali", text_alignment="center", divider="green")
st.write("*Silahkan masuk menggunakan akun DwTix anda*")

# data di sini dalam bentuk dictionary, untuk detail cek di user.py ya
user_by_name = user_data_by_username()
# ga boleh hapus untuk asdos nanti cek perubahan password
st.write(user_by_name)
# form -> username dan password (tipe password) 2 2 nya wajib pake required ya 
username_input = st.text_input("Username", placeholder="Masukkan username", key="input_username")
password_input = st.text_input("Password", placeholder="Masukkan password", type="password", key="input_password")
# hint -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# tombol login
if st.button(label="Login", type="primary"):
 
    # cek apakah username ada di database
    if username_input in user_by_name:
        user = user_by_name[username_input]
 
        # cek apakah password cocok
        if password_input == user["password"]:
 
            # simpan info login ke session state
            st.session_state.logged_in = True
            st.session_state.username  = username_input
            st.session_state.password  = password_input
 
            # cek role
            if user["role"] == "Peserta":
                # peserta langsung ke halaman event, tidak boleh ke dashboard
                st.switch_page("pages/event.py")
            else:
                # admin ke dashboard
                st.switch_page("pages/dashboard.py")
        else:
            st.error("Login gagal! Silahkan coba kembali")
    else:
        st.error("Login gagal! Silahkan coba kembali")
 
# submit -> st.button(label="Login", type="primary")
#  Kondisi -> jika role yang login peserta alihin nya ke event langsung dan ga boleh buka dashboard
# Kalau salah st.error "Login gagal! Silahkan coba kembali"


