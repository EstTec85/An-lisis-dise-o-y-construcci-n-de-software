import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Datos de conexión
host = "aitest.cnugu40qabl8.us-east-2.rds.amazonaws.com"
port = "5432"
database = "testai"
user = "postgres"
password = "AItec2024"

# Conectar a la base de datos
def get_connection():
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        return conn
    except Exception as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return None

# Función para insertar un nuevo usuario
def create_user(username, email, password_hash):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (username, email, password_hash, created_at)
                    VALUES (%s, %s, %s, %s) RETURNING id;
                """, (username, email, password_hash, datetime.utcnow()))
                user_id = cur.fetchone()[0]
                conn.commit()
                st.success(f"Usuario creado con ID: {user_id}")
        except Exception as e:
            st.error(f"Error al crear el usuario: {e}")
        finally:
            conn.close()

# Función para validar login
def login_user(username, password_hash):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM users WHERE username = %s AND password_hash = %s;
                """, (username, password_hash))
                user = cur.fetchone()
                if user:
                    st.success(f"Bienvenido, {user['username']}!")
                else:
                    st.error("Credenciales incorrectas.")
        except Exception as e:
            st.error(f"Error al iniciar sesión: {e}")
        finally:
            conn.close()

# Función para enviar clave temporal por correo
# Función para enviar clave temporal por correo
def send_temporary_password(email, temp_password):
    EMAIL_USER = "tu_email@gmail.com"
    EMAIL_PASS = "contraseña_de_aplicacion_generada"

    msg = MIMEText(f"Tu nueva contraseña temporal es: {temp_password}")
    msg['Subject'] = "Recuperación de Contraseña"
    msg['From'] = EMAIL_USER
    msg['To'] = email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            st.success("Correo enviado correctamente.")
    except Exception as e:
        st.error(f"Error al enviar el correo: {e}")


# Función para recuperar contraseña
def recover_password(email):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
                user = cur.fetchone()
                if user:
                    temp_password = "temp1234"  # Contraseña temporal fija (puedes cambiarla)
                    send_temporary_password(email, temp_password)

                    # Actualizar contraseña temporal en la base de datos
                    cur.execute("""
                        UPDATE users SET password_hash = %s WHERE email = %s;
                    """, (temp_password, email))
                    conn.commit()
                    st.success("Contraseña temporal enviada por correo.")
                else:
                    st.error("No se encontró un usuario con ese correo.")
        except Exception as e:
            st.error(f"Error al recuperar la contraseña: {e}")
        finally:
            conn.close()

# Página principal de login, registro y recuperación de contraseña
def show_login_page():
    st.title("TestAI")

    # Selección de modo: Login, Registro o Recuperar Contraseña
    mode = st.selectbox("Selecciona una opción", ["Iniciar Sesión", "Registrarse", "Recuperar Contraseña"])

    if mode == "Registrarse":
        st.subheader("Registro de Usuario")
        username = st.text_input("Nombre de Usuario")
        email = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")

        if st.button("Registrar"):
            if username and email and password:
                create_user(username, email, password)
            else:
                st.error("Por favor completa todos los campos.")
            

    elif mode == "Iniciar Sesión":
        st.subheader("Iniciar Sesión")
        username = st.text_input("Nombre de Usuario", key="login_username")
        password = st.text_input("Contraseña", type="password", key="login_password")

        if st.button("Iniciar Sesión"):
            login_user(username, password)


    elif mode == "Recuperar Contraseña":
        st.subheader("Recuperar Contraseña")
        email = st.text_input("Correo Electrónico")

        if st.button("Recuperar"):
            if email:
                recover_password(email)
            else:
                st.error("Por favor ingresa tu correo.")
    
    
   

