import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set structure of the site
header = st.container()
crisis_indicator = st.container()
dataset = st.container()


# Cache selected dataset
@st.cache
def get_data(filename):
    stock_data = pd.read_csv(filename, sep=',')
    return stock_data


with header:
    st.title('Welcome to the irrationality project!')
    st.text('In this project I look into the implementation of irrationality')
    st.text('into the portfolio allocation process.')
    st.text('')


with crisis_indicator:
    st.header("1. Let's have a look at the economic outlook")
    
    cp = pd.read_csv('data/crisis_probability.txt', sep=" ", header=None)
    x = cp.values[0]
    if x == 1:
        st.success('The probability of a severe econonomic crisis within the next six months is minimal')
    else:
        st.error('! The probability of a severe econonomic crisis within the next six months is substantial !')
  
    st.text('')


with dataset:
    st.header("2. Let's analyze the stocks by region & quartile")
    st.text('')
   
    sel_col, disp_col = st.columns(2)
    region = sel_col.selectbox('Which region do you want to analyze?', options=['US 500', 'Germany 40'], index=0)
    quartile = sel_col.selectbox('Which quartile do you want to analyze?', options=['All', 'First', 'Second', 'Third', 'Fourth'], index = 0)

    st.text('')
    st.text('')

    if region == 'US 500':

        df = pd.read_csv('data/us500.csv')
        stock_data = pd.DataFrame([df.Name, df.Ticker]).transpose()
        boundaries = np.linspace(0, stock_data.shape[0], 5).round()
        zero, first, second, third, fourth = int(boundaries[0]), int(boundaries[1]), int(boundaries[2]), int(boundaries[3]), int(boundaries[4]) 
   
    else: 

        df = pd.read_csv('data/germany40.csv')
        stock_data = pd.DataFrame([df.Name, df.Ticker]).transpose()
        boundaries = np.linspace(0, stock_data.shape[0], 5).round()
        zero, first, second, third, fourth = int(boundaries[0]), int(boundaries[1]), int(boundaries[2]), int(boundaries[3]), int(boundaries[4]) 

    if quartile == 'All':
        data_selected = stock_data[:]
    elif quartile == 'First':
        data_selected = stock_data[zero:first]
    elif quartile == 'Second':
        data_selected = stock_data[first:second]
    elif quartile == 'Third':
        data_selected = stock_data[second:third]
    elif quartile == 'Fourth':
        data_selected = stock_data[third:fourth]

    st.table(data=data_selected)