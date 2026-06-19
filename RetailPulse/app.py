import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="wide"
)

st.title("📊 RetailPulse Dashboard")
st.write("AI-Powered Customer Analytics & Demand Forecasting")

# Function to locate files
def find_file(filename):
    possible_paths = [
        filename,
        f"RetailPulse/{filename}",
        f"./{filename}",
        os.path.join(os.getcwd(), filename)
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(f"{filename} not found")

try:
    customers_file = find_file("customers.xls")
    sales_file = find_file("sales_data.xls")
    inventory_file = find_file("inventory.xls")

    customers = pd.read_csv(customers_file)
    sales = pd.read_csv(sales_file)
    inventory = pd.read_csv(inventory_file)

    st.success("Datasets loaded successfully!")

    st.header("📈 Project Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", len(customers))
    col2.metric("Total Sales Records", len(sales))
    col3.metric("Total Products", len(inventory))

    st.header("👥 Customer Dataset")
    st.dataframe(customers.head())

    st.header("💰 Sales Dataset")
    st.dataframe(sales.head())

    st.header("📦 Inventory Dataset")
    st.dataframe(inventory.head())

    st.header("📋 Dataset Information")
    st.write("Customers Shape:", customers.shape)
    st.write("Sales Shape:", sales.shape)
    st.write("Inventory Shape:", inventory.shape)

except Exception as e:
    st.error(f"Error: {e}")

    st.subheader("Current Directory")
    st.code(os.getcwd())

    st.subheader("Available Files")
    for root, dirs, files in os.walk("."):
        st.write(f"📁 {root}")
        for file in files:
            st.write(f"   📄 {file}")
