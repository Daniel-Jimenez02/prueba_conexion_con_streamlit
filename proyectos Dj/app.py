import streamlit as str

# 1. Configurar la página (opcional, para cambiar el título de la pestaña)
str.set_page_config(page_title="Mi Página Web", layout="wide")

# 2. Leer el archivo HTML existente
with open("proyectos Dj/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. Renderizar el HTML en Streamlit (permitiendo scripts y estilos CSS internos)
str.components.v1.html(html_content, height=800, scrolling=True)
