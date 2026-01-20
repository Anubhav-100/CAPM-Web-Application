import plotly.express as px
import numpy as np

# Function to plot interactive CAPM graph
def interactive_capm_plot(df, title, yaxis):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x= df['Date'], y=df[i], mode='lines', name=i)
    fig.update_layout(width = 450, margin = dict(l=20, r=20, t=50, b=20),
                    legend = dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                    title=title,
                    xaxis_title="Date",
                    yaxis_title=yaxis,
                    hovermode="x unified")
    return fig

# Function to normalize the prices based on the initial price
def normalize_prices(df):
    for i in df.columns[1:]:
        df[i] = df[i] / df[i].iloc[0]
    return df 

# Function to calculate daily returns
def daily_returns(df):
    for i in df.columns[1:]:
        for j in range(1, len(df)): 
            df[i][j] = ((df[i][j] - df[i][j-1]) / df[i][j-1]) * 100
        df[i][0] = 0  # First day return is set to 0 
    return df

# Function to calculate beta values
def calculate_beta(stocks_daily_return, stock):
    rm = stocks_daily_return['SP500'].mean()*252  # Annualized market return
    
    b, a = np.polyfit(stocks_daily_return['SP500'], stocks_daily_return[stock], 1)
    return b,a
          

# Function to calculate average returns
def average_returns(df):    
    avg_returns = {}
    for i in df.columns[1:]:
        avg_returns[i] = df[i].mean()
    return avg_returns 