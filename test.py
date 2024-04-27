import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

NAME = "XRP-USD"

data = yf.download(tickers=NAME, period='24h', interval='15m')
#달러에 대한 가격, 기간, 간격

fig = go.Figure(data=go.Candlestick(
    x=data.index,
    open=data["Open"],
    high=data["High"],
    low=data["Low"],
    close=data["Close"],
))

st.plotly_chart(fig)