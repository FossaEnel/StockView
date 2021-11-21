import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Ali's Finance Dashboard")

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD','ETH-USD','DIS','SHIB-USD','ADA-USD','DOSE-USD','GME','AMC','XRP-USD','SOL1-USD','ADA-CDA' )

dropdown = st.multiselect('Pick your assets',tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End',value = pd.to_datetime('today'))

def ret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = ret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Return of {}'.format(dropdown))
    st.line_chart(df)