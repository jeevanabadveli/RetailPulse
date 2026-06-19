# RetailPulse – AI-Powered Customer Analytics & Demand Forecasting

## Overview

RetailPulse is a data analytics and machine learning project developed to help retail businesses understand customer behavior, predict customer churn, forecast future demand, and optimize inventory management.

The project uses Python, Pandas, Scikit-Learn, Matplotlib, and Streamlit to transform retail data into actionable business insights.

---

## Features

### Customer Analytics

* Customer Segmentation using K-Means Clustering
* Customer Behavior Analysis
* Customer Churn Prediction using Random Forest Classifier

### Demand Forecasting

* Revenue Trend Analysis
* Future Sales Forecasting
* Demand Prediction Visualization

### Inventory Optimization

* Reorder Status Detection
* Suggested Reorder Quantity Calculation
* Inventory Risk Analysis

### Dashboard

* Interactive Streamlit Dashboard
* Dataset Overview
* Key Business Metrics

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Jupyter Notebook

---

## Project Structure

```text
RetailPulse/
│
├── app.py
├── requirements.txt
├── README.md
├── _RetailPulse_Project.ipynb
│
├── customers.xls
├── sales_data.xls
├── inventory.xls
│
├── customer_segments.xls
├── forecast_results.xls
├── inventory_recommendations.xls
│
├── age_distribution.png
├── churn_distribution.png
├── customer_segmentation.png
├── demand_forecast.png
├── inventory_reorder.png
└── revenue_trend.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jeevanabadveli/RetailPulse.git
cd RetailPulse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

---

## Machine Learning Models

### Customer Segmentation

* Algorithm: K-Means Clustering
* Features:

  * Age
  * Previous Purchases
  * Review Rating

### Churn Prediction

* Algorithm: Random Forest Classifier
* Model Accuracy: 78.5%

### Demand Forecasting

* Algorithm: Linear Regression
* Forecast Horizon: 30 Days

---

## Results

### Customer Segmentation

Customers were grouped into multiple clusters based on purchasing behavior and demographics.

### Churn Prediction

The Random Forest model achieved an accuracy of approximately 78.5%.

### Demand Forecasting

Future sales demand was predicted using historical revenue trends.

### Inventory Optimization

Products requiring replenishment were identified and recommended order quantities were generated.

---

## Business Benefits

* Improved customer understanding
* Reduced customer churn
* Better demand planning
* Inventory cost optimization
* Data-driven decision making

---

## Future Enhancements

* Real-time analytics dashboard
* Advanced forecasting models (Prophet, LSTM)
* Automated inventory alerts
* Cloud deployment
* Interactive business intelligence reports

---


