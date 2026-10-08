import streamlit as st
from user import user_data_by_username

# set tab title -> https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation silahkan kalau mau baca karena gabut awoaowawo
st.set_page_config(page_title="DwTix - Login")

# deklarasi sesi username, password, dan status login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

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
username_input = st.text_input("username")
password_input = st.text_input("password")

# hint -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input

# submit -> st.button(label="Login", type="primary")

if st.button("Login"): 
    for nama, data in user_by_name.items():
#  Kondisi -> jika role yang login peserta alihin nya ke event langsung dan ga boleh buka dashboard
        if username_input == nama and password_input == data["password"]:
            if data["role"] == "Peserta":
                st.session_state['logged_in'] = True
                st.switch_page("pages/event.py")
            if data["role"] == "Admin":
                st.session_state['logged_in'] = True
                st.switch_page("pages/dashboard.py")

        else:
            st.error("Login Gagal! Silahkan coba kembali")

# Kalau salah st.error "Login gagal! Silahkan coba kembali"


