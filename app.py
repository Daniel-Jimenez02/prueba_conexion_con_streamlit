import os
import streamlit as str

str.set_page_config(page_title="Mi Página Web", layout="wide")

# Forzar la ruta absoluta a la raíz de la app en la nube
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

str.components.v1.html(html_content, height=800, scrolling=True)
