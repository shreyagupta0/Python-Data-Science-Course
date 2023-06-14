#streamlit run 'data_science\wapp.py'



import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#loading the database
@st.cache_data
def load():
    df = pd.read_csv('data__science/pokemon.csv' , index_col=1)
    df.drop(columns=['#'] , inplace = True)
    return df

# main ui code

st.set_page_config(
    page_title='Pokemon Data Viz',
    layout='wide'
)


# - get the data
with st.spinner ('laoding data....'):
    df = load()
    st.balloons()


#2column
c1 , c2 = st.columns(2)
c1.dataframe(df)

c2.metric('Total Pokemon' , df.shape[0] , '👻')
cnt_legendary= df['type1'].value_counts()[1]
cnt_types = df  

st.dataframe(df)    #to show data

#viz
st.header('Pokemon Graphically')
c1,c2 = st.columns[4,9]


