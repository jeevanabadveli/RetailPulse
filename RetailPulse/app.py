import streamlit as st
import pandas as pd

st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")

st.title("📊 RetailPulse Dashboard")
st.write("AI-Powered Customer Analytics & Demand Forecasting")

# Load datasets
customers = pd.read_csv("customers.xls")
sales = pd.read_csv("sales_data.xls")
inventory = pd.read_csv("inventory.xls")

# Metrics
st.header("Project Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(customers))
col2.metric("Total Sales Records", len(sales))
col3.metric("Total Products", len(inventory))

# Customer Data
st.header("Customer Dataset")
st.dataframe(customers.head())

# Sales Data
st.header("Sales Dataset")
st.dataframe(sales.head())

# Inventory Data
st.header("Inventory Dataset")
st.dataframe(inventory.head())

st.header("Dataset Shapes")
st.write("Customers:", customers.shape)
st.write("Sales:", sales.shape)
st.write("Inventory:", inventory.shape)