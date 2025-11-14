import streamlit as st
import pandas as pd
from modules.comparador import extraer_tablas, comparar_elementos
from modules.generador import generar_ruta_estrategica

st.set_page_config(page_title="Integrador PEI", layout="wide")
st.title("🧭 Integrador PEI: Comparador + Ruta Estratégica Automática")

# === PASO 1: Carga del archivo del usuario ===
st.header("📘 1. Carga del documento PEI")

archivo_usuario = st.file_uploader("Sube tu archivo PEI (Word o PDF)", type=["docx", "pdf"])

if archivo_usuario:
    with st.spinner("Extrayendo tablas del documento..."):
        tablas_extraidas = extraer_tablas(archivo_usuario)
    
    st.success("✅ Tablas extraídas correctamente")
    for nombre, df in tablas_extraidas.items():
        st.subheader(nombre)
        st.dataframe(df, use_container_width=True)

    # === PASO 2: Comparación con estándares ===
    with st.spinner("Comparando elementos con las tablas estándar..."):
        resultado_comparacion, oei_extraidos, aei_extraidos = comparar_elementos(tablas_extraidas)

    st.success("✅ Comparación completada")
    st.write("**Elementos OEI y AEI extraídos del documento:**")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("OEI")
        st.dataframe(oei_extraidos, use_container_width=True)
    with col2:
        st.subheader("AEI")
        st.dataframe(aei_extraidos, use_container_width=True)

    # === PASO 3: Generación automática de la Ruta Estratégica ===
    with st.spinner("Generando la Ruta Estratégica..."):
        ruta_df = generar_ruta_estrategica(oei_extraidos, aei_extraidos)

    st.header("🗺️ 2. Ruta Estratégica Generada Automáticamente")
    st.dataframe(ruta_df, use_container_width=True)

    st.download_button(
        label="💾 Descargar Ruta Estratégica (Excel)",
        data=ruta_df.to_csv(index=False).encode("utf-8"),
        file_name="ruta_estrategica.csv",
        mime="text/csv"
    )
