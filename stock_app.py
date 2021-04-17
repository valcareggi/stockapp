#### Importing required modules

import streamlit as st
import pandas as pd
import fix_yahoo_finance as yf

#### Getting user inputs

def get_input():
    ticker = st.sidebar.text_input("Ticker", "PETR4")
    start_date = st.sidebar.text_input("Start Date", "2000-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-01-02")
    
    return(start_date, end_date, ticker)

#### Getting data from yahoo finance

def get_data(symbol, start_date, end_date):
    ticker = str(symbol)+'.SA'
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    df = yf.download(ticker, start=start, end=end)   

    return df


# Asking user for inputs
start, end, ticker = get_input()

#Getting data based on user inputs
df = get_data(ticker, start, end)

#Displaying the Adjusted Close Price
st.header(ticker +" "+ "Adj Close \n")
st.line_chart(df['Adj Close'])

#Displaying the Volume
st.header(ticker +" "+ "Volume \n")
st.line_chart(df['Volume'])

#Displaying 30 days moving average 
st.header('MA(30)')
st.write(round(df['Adj Close'].rolling(window=30).mean(),2).dropna())
st.header('Graph: MA(30)')
st.line_chart(round(df['Adj Close'].rolling(window=30).mean(),2).dropna())


    

