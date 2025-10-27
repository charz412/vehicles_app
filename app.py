import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Vehicles Dashboard", layout="wide")

# Encabezado
st.header("🚗 Vehículos en venta – Mini Dashboard (Streamlit + Plotly)")

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Mostrar info básica
st.write(f"Filas: {len(df):,}")
st.write("Columnas:", list(df.columns))

# Selección de columnas numéricas
numeric_cols = df.select_dtypes(include="number").columns.tolist()
hist_col = st.selectbox("Columna para histograma", options=numeric_cols, index=0)
scatter_x = st.selectbox("Eje X (dispersión)", options=numeric_cols, index=0)
scatter_y = st.selectbox("Eje Y (dispersión)", options=numeric_cols, index=min(1, len(numeric_cols)-1))

# Casillas de verificación
build_hist = st.checkbox("Construir histograma")
build_scatter = st.checkbox("Construir gráfico de dispersión")

# Gráficos
if build_hist:
    st.subheader("Histograma")
    fig_h = px.histogram(df, x=hist_col, nbins=40, title=f"Distribución de {hist_col}")
    st.plotly_chart(fig_h, use_container_width=True)

if build_scatter:
    st.subheader("Gráfico de dispersión")
    fig_s = px.scatter(df, x=scatter_x, y=scatter_y, opacity=0.6,
                       title=f"{scatter_x} vs {scatter_y}")
    st.plotly_chart(fig_s, use_container_width=True)

st.caption("Selecciona las casillas para ver los gráficos.")