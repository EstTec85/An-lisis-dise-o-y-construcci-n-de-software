import streamlit as st
from pages.login import show_login_page  # Importar la página de login
from pages.code_analyzer import show_code_analyzer_page  # Importar la página de análisis

# Inicializar el estado de la sesión
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False  # Estado inicial

# Función para cerrar sesión
def logout():
    st.session_state['authenticated'] = False  # Restablecer autenticación
    st.experimental_rerun()  # Refrescar la app para redirigir al login

# Lógica para mostrar las páginas según el estado de la sesión
def main():
    if st.session_state['authenticated']:
       # st.switch_page("pages/code_analyzer.py")
        show_code_analyzer_page()
    else:
        # Mostrar la página de análisis de código si está autenticado
        
        show_login_page()

        # Botón para cerrar sesión
        if st.button("Cerrar Sesión"):
            logout()

# Ejecutar la aplicación principal
if __name__ == "__main__":
    main()




