import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import pandas_datareader.data as web
import CAPM_functions as capm

st.set_page_config(page_title="CAPM Return Calculator",
                   page_icon ="chart_with_upwards_trend",
                   layout="wide")

st.title("Capital Asset Pricing Model (CAPM) Return Calculator")

# getting input from user

col1, col2 = st.columns([1, 1])
with col1: 
    stocks_list = st.multiselect("Choose atleast 4 stocks", 
                options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "DIS", "NFLX", "ADBE", "PYPL", "INTC", "CSCO", "CMCSA", "PEP", "KO", "NKE", "MCD"],
                default=["AAPL", "MSFT", "GOOGL", "AMZN"],
                key="stocks") 
with col2: 
    year = st.number_input("Number of years", min_value=1, max_value=10, key="years")
    
# downloading data for SP500 as market index
try:
    end = datetime.date.today()
    try:
        start = datetime.date(end.year - year, end.month, end.day)
    except ValueError:
        # handles Feb 29 for non-leap years
        start = datetime.date(end.year - year, end.month, 28)

    SP500 = web.DataReader(['sp500'], 'fred', start, end)

    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock, period = f"{year}y")
        stocks_df[f'{stock}'] = data['Close']

    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)

    SP500.columns = ['Date', 'SP500']
    stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
    stocks_df['Date'] = stocks_df['Date'].dt.date
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    stocks_df = pd.merge(stocks_df, SP500, on='Date', how='inner')


    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Stocks Data (Earliest)")
        st.dataframe(stocks_df.head(), use_container_width=True)
    with col2:
        st.subheader("Stocks Data (Latest)")
        st.dataframe(stocks_df.tail(), use_container_width=True)
        
    st.markdown("---"*20)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("CAPM Stock Returns Over Time")
        capm_fig = capm.interactive_capm_plot(stocks_df, title="CAPM Stock Returns Over Time", yaxis="Stock Prices")
        st.plotly_chart(capm_fig, use_container_width=True) 
        
    with col2:
        st.subheader("Normalized Stock Prices Over Time")
        normalize_stocks_df = capm.normalize_prices(stocks_df.copy())
        normalize_capm_fig = capm.interactive_capm_plot(normalize_stocks_df, title="Normalized Stock Prices Over Time", yaxis="Normalized Prices")
        st.plotly_chart(normalize_capm_fig, use_container_width=True)
        
    st.markdown("---"*20)

    stocksdaily_return = capm.daily_returns(stocks_df.copy())

    beta = {}
    alpha = {}

    for i in stocksdaily_return.columns:
        if i != 'Date' and i != 'SP500':
            b, a = capm.calculate_beta(stocksdaily_return, i)
            beta[i] = b
            alpha[i] = a

    beta_df = pd.DataFrame(columns = ['Stock', 'Beta value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta value'] = [str(round(i,2)) for i in beta.values()]


    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Calculate Beta Values")
        st.dataframe(beta_df, use_container_width=True)
        
    rf = 0
    rm = stocksdaily_return['SP500'].mean()*252  # Annualized market return

    return_df = pd.DataFrame()
    return_value = []
    for stock, value in beta.items():
        return_value.append(str(round(rf + value * (rm - rf),2)))
    return_df['Stock'] = beta.keys()

    return_df['Expected Return value'] = return_value

    with col2:
        st.subheader("Expected Return based on CAPM")
        st.dataframe(return_df, use_container_width=True)
        
except Exception as e:
    st.error("Error in fetching data. Please ensure you have selected atleast 4 stocks.")