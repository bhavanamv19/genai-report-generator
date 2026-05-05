import streamlit as st
import pandas as pd
import os
from data_analyzer import analyze_data
from report_generator import generate_insights
from pdf_generator import create_pdf

os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="GenAI Business Report Generator", page_icon="📊", layout="wide")

st.title("📊 GenAI Business Report Generator")
st.markdown("Upload any CSV or Excel file → Get an AI-powered PDF business report instantly")
st.markdown("---")

col_side, col_main = st.columns([1, 3])

with col_side:
    st.markdown("### ⚙️ Settings")
    business_context = st.selectbox(
        "Business Context",
        ["Sales", "Finance", "HR", "Marketing", "Operations", "Healthcare", "E-Commerce", "Retail"]
    )
    st.markdown("---")
    st.markdown("### 📌 How to Use")
    st.markdown("1. 📁 Upload CSV or Excel\n2. ⚙️ Select context\n3. 🚀 Click Generate\n4. 📥 Download PDF")

with col_main:
    st.markdown("### 📁 Upload Your Data File")
    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success(f"✅ {uploaded_file.name} — {df.shape[0]} rows × {df.shape[1]} columns")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📋 Data Preview")
            st.dataframe(df.head(10), use_container_width=True)
        with col2:
            st.markdown("#### 📈 Quick Statistics")
            st.dataframe(df.describe(), use_container_width=True)

        st.markdown("---")

        if st.button("🚀 Generate AI Report", use_container_width=True):
            with st.spinner("🤖 Generating AI insights..."):
                analysis = analyze_data(df)
                insights = generate_insights(analysis, business_context)
                pdf_path = create_pdf(insights, analysis)

            st.success("✅ Report Generated!")
            st.balloons()

            st.markdown("#### 🤖 AI Insights Preview")
            st.markdown(insights)
            st.markdown("---")

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download PDF Report",
                    data=f,
                    file_name=f"{business_context}_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    else:
        st.info("👆 Please upload a CSV or Excel file to get started!")