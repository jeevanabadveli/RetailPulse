import streamlit as st
import pandas as pd
import os

# Page settings
st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="wide"
)

st.title("📊 RetailPulse Dashboard")
st.write("AI-Powered Customer Analytics & Demand Forecasting")

# Debug Section
st.sidebar.header("Debug Information")
st.sidebar.write("Current Working Directory:")
st.sidebar.code(os.getcwd())

st.sidebar.write("Files in Current Directory:")
try:
    st.sidebar.write(os.listdir("."))
except Exception as e:
    st.sidebar.error(str(e))

# Show complete folder structure
st.sidebar.write("Folder Structure:")
for root, dirs, files in os.walk("."):
    st.sidebar.write(f"📁 {root}")
    for file in files:
        st.sidebar.write(f"   📄 {file}")

# Load data
try:
    customers = pd.read_csv("customers.xls")
    sales = pd.read_csv("sales_data.xls")
    inventory = pd.read_csv("inventory.xls")

    st.success("Datasets loaded successfully!")

    # Metrics
    st.header("📈 Project Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Customers", len(customers))

    with col2:
        st.metric("Total Sales Records", len(sales))

    with col3:
        st.metric("Total Products", len(inventory))

    # Customer Data
    st.header("👥 Customer Dataset")
    st.dataframe(customers.head())

    # Sales Data
    st.header("💰 Sales Dataset")
    st.dataframe(sales.head())

    # Inventory Data
    st.header("📦 Inventory Dataset")
    st.dataframe(inventory.head())

    # Dataset Shapes
    st.header("📋 Dataset Information")

    st.write("Customers Shape:", customers.shape)
    st.write("Sales Shape:", sales.shape)
    st.write("Inventory Shape:", inventory.shape)

except Exception as e:
    st.error(f"Error loading files: {e}")

    st.subheader("Current Directory")
    st.code(os.getcwd())

    st.subheader("Files Found")
    try:
        st.write(os.listdir("."))
    except Exception as err:
        st.write(err)

st.markdown("---")
st.write("RetailPulse Dashboard")
