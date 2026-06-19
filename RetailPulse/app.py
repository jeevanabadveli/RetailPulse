import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="wide"
)

# Debug information
st.sidebar.header("Debug Information")
st.sidebar.write("Current Directory:")
st.sidebar.write(os.getcwd())

st.sidebar.write("Files Available:")
st.sidebar.write(os.listdir())

# Title
st.title("📊 RetailPulse Dashboard")
st.write("AI-Powered Customer Analytics & Demand Forecasting")

# Load datasets
try:
    customers = pd.read_csv("customers.xls")
    sales = pd.read_csv("sales_data.xls")
    inventory = pd.read_csv("inventory.xls")

    # Metrics
    st.header("📈 Project Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Customers", len(customers))

    with col2:
        st.metric("Total Sales Records", len(sales))

    with col3:
        st.metric("Total Products", len(inventory))

    # Customer Dataset
    st.header("👥 Customer Dataset")
    st.dataframe(customers.head())

    # Sales Dataset
    st.header("💰 Sales Dataset")
    st.dataframe(sales.head())

    # Inventory Dataset
    st.header("📦 Inventory Dataset")
    st.dataframe(inventory.head())

    # Dataset Information
    st.header("📋 Dataset Shapes")

    st.write("Customers:", customers.shape)
    st.write("Sales:", sales.shape)
    st.write("Inventory:", inventory.shape)

except Exception as e:
    st.error(f"Error loading files: {e}")

    st.write("Current directory:")
    st.code(os.getcwd())

    st.write("Files available in this directory:")
    st.write(os.listdir())

# Footer
st.markdown("---")
st.write("RetailPulse Project Dashboard")
