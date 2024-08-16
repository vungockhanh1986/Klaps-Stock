import streamlit as st
import pandas as pd
import plotly_express as px

@st.cache_data

def load_data():
    df = pd.read_csv('all_stocks_5yr.csv',
                     index_col='date')
    
    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns
    
    text_df = df.select_dtypes(['object'])
    text_columns = text_df.columns
    
    stock_column = df['Name']
    
    unique_stocks = stock_column.unique()
    
    return df, numeric_cols, text_columns, unique_stocks

df, numeric_cols, text_columns, unique_stocks = load_data()

st.title(":rainbow[KHÁNH-CHÓ 's Stocks Dashboard]")

st.sidebar.title('Settings')

st.sidebar.subheader('Timeseries Settings')

feature_selection = st.sidebar.multiselect(label='Features to plot',
                                           options=numeric_cols)

stock_ticker = st.sidebar.selectbox(label='Stock Ticker',
                                    options=unique_stocks)

check_box = st.sidebar.checkbox(label='Display the Dataset')

stock_df = df[df['Name'] == stock_ticker]


try:
    plotly_figure = px.line(
                    data_frame=stock_df,
                    x=stock_df.index,
                    y=feature_selection,
                    title='Timeline of ' + str(stock_ticker) + ' prices:')

    st.plotly_chart(plotly_figure)

except Exception as e:
    print(e)


if check_box and feature_selection!=[] :
    st.write(':blue[All OUR DATASETS AS:]')
    st.write(df)
    
    st.write(':green[YOU SELECTED THE STOCK:] ' + str(stock_ticker))
    display = stock_df[feature_selection]
    st.write(display)