import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.pipeline import run_query_pipeline

st.set_page_config(page_title="DataCopilot", layout="wide")
st.title("🤖 DataCopilot – AI SQL Assistant")

# -------------------------
# SESSION
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

schema = None

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.warning("Standard parsing failed, trying robust mode...")

        df = pd.read_csv(
            uploaded_file,
            engine="python",           # more flexible parser
            on_bad_lines="skip"        # skip problematic rows
        )

    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # Save to SQLite
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "data", "sap_mock.db")

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("UserTable", conn, if_exists="replace", index=False)
    conn.close()

    # Generate schema
    schema = "UserTable(" + ", ".join(df.columns) + ")"

    st.info(f"Detected Schema: {schema}")

# -------------------------
# INPUT
# -------------------------
query = st.text_input("Ask a question about your data:")

if st.button("Run Query") and query:
    output = run_query_pipeline(query, schema)

    st.session_state.history.append({
        "query": query,
        "output": output
    })

# -------------------------
# KPI
# -------------------------
def show_kpis(df):
    if df is None or df.empty:
        return

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))

    if "Revenue" in df.columns:
        col2.metric("Total Revenue", f"{df['Revenue'].sum():,.0f}")
        col3.metric("Max Revenue", f"{df['Revenue'].max():,.0f}")

# -------------------------
# CHART
# -------------------------
def show_chart(df):
    if df is None or df.empty:
        return

    if len(df.columns) >= 2:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        st.plotly_chart(fig, use_container_width=True)

# -------------------------
# DISPLAY
# -------------------------
for chat in reversed(st.session_state.history):

    st.markdown("---")
    st.subheader("🧑 Query")
    st.write(chat["query"])

    if "error" in chat["output"]:
        st.error(chat["output"]["error"])
        continue

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 SQL")
        st.code(chat["output"]["sql"], language="sql")

    with col2:
        st.subheader("💬 Explanation")
        st.write(chat["output"]["explanation"])

    df = chat["output"]["result"]

    st.subheader("📊 Results")
    st.dataframe(df)

    show_kpis(df)
    show_chart(df)