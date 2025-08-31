import streamlit as st
import pandas as pd

# URL del nuevo archivo CSV en GitHub
# Reemplaza 'tu_usuario', 'nombre_del_repositorio' y 'ruta_al_nuevo_archivo.csv'
# con los datos de tu repositorio
url = 'https://raw.githubusercontent.com/consupalabrahoy-cloud/diccionariobiblico/refs/heads/main/Diccionario%20-%20Diccionario.csv'

@st.cache_data
def load_data(url):
    """
    Carga los datos desde el CSV de GitHub.
    """
    df = pd.read_csv(url)
    return df

try:
    # Cargar los datos
    df = load_data(url)

    # Crear una columna combinada para el desplegable
    # Se combinan 'Tema Bíblico', 'Palabra y Transliteración' y 'Traducción literal'
    df['Opciones'] = (
        df['Tema Bíblico'] + ' - ' +
        df['Palabra y Transliteración'] + ' (' +
        df['Traducción literal'] + ')'
    )

    # Título de la aplicación
    st.title("Diccionario Temático")
    st.markdown("---")

    # Crear el desplegable (select box)
    opcion_seleccionada = st.selectbox(
        'Selecciona un tema, palabra y traducción:',
        options=df['Opciones']
    )

    # Filtrar el DataFrame para obtener la fila seleccionada
    fila_seleccionada = df[df['Opciones'] == opcion_seleccionada].iloc[0]

    # Mostrar la información completa de la fila seleccionada
    st.subheader("Información de la palabra seleccionada")
    st.markdown("---")

    # Usar un bucle para mostrar todas las columnas y sus valores
    for columna, valor in fila_seleccionada.items():
        if columna not in ['Opciones']: # Evita mostrar la columna 'Opciones'
            st.write(f"**{columna}:** {valor}")

except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {e}")

    st.info("Asegúrate de que la URL del archivo CSV en GitHub sea correcta y accesible.")
