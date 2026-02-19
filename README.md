📊 **CAPM Web Application**

A professional financial analytics web application built using Streamlit that calculates Expected Stock Returns using the Capital Asset Pricing Model (CAPM) and visualizes stock performance against the S&P 500 benchmark.
This project demonstrates practical implementation of financial modeling, regression-based beta estimation, and interactive data visualization.

🚀 **Overview**

The CAPM Web Application allows users to:
- Select multiple stocks
- Define a historical time range
- Compare stock performance with the market (S&P 500)
- Calculate Beta using linear regression
- Estimate expected returns using the CAPM model
- Visualize price trends and normalized performance interactively

This project is ideal for learning:
- Financial Modeling
- Quantitative Finance Basics
- Risk & Return Analysis
- Data Visualization
- Streamlit Dashboard Development

🧠 **Financial Model: CAPM**

The application implements the Capital Asset Pricing Model (CAPM):
                        𝐸(𝑅𝑖)=𝑅𝑓+𝛽𝑖(𝑅𝑚−𝑅𝑓)

Where:
- E(Ri) → Expected return of stock
- Rf → Risk-free rate (currently assumed 0)
- βi (Beta) → Sensitivity of stock to market movements
- Rm → Expected market return (Annualized S&P 500 return)

✨ Key Features
📌 Data Collection

Fetches stock data using Yahoo Finance API

Retrieves S&P 500 data from FRED (Federal Reserve Economic Data)

Automatically merges and aligns time-series data

📈 Visualization

Interactive price charts (Plotly)

Normalized price comparison

Unified hover mode for better time-series comparison

📊 Financial Calculations

Daily returns computation

Beta estimation using linear regression

Annualized market return calculation

Expected return calculation via CAPM formula

📋 Output Tables

Historical stock data preview

Beta values per stock

CAPM-based expected return per stock

🛠️ Technology Stack
Category	Tools Used
Language	Python
Web Framework	Streamlit
Data Processing	Pandas, NumPy
Data Source	yFinance, pandas-datareader
Visualization	Plotly
Financial Modeling	CAPM, Linear Regression
