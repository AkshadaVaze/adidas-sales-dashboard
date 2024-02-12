import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
st.set_page_config(layout="wide")
selected_input = st.sidebar.selectbox("select",['Description and data', 'Analysis'])
df=pd.read_excel("Adidas.xlsx")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
col1,col2=st.columns([0.1,0.9])
with col1:
    st.image("photo.jpeg",width=100)
with col2:
    st.markdown("""
      <style>
      .title-test {
      font-weight:bold;
      padding:5px;
      border-radius:6px;
      }
      </style>
      <center><h1 class="title-test">Adidas Interactive Sales Dashboard</h1></center>""", unsafe_allow_html=True)
    st.divider()
    col4,col5=st.columns(2)

if selected_input == 'Description and data':
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:  \n {box_date}")
    st.markdown("The dataset offers a comprehensive view of Adidas product sales across various retailers and regions.Each row represents a sales transactions,with details including the retailers name and ID, the date of transactions, geographical information such as region, state, city as well as specifies about products sold, such as its name, price per unit, quality sold. Additionally, financial metricks such as total sales, operating profit, operating margin, shedding light on financial performance of each trasactions. The data set also includes information about the sales methods employed for each transaction. This rich data set enables in depth analysis of Adidas sales trends, profitability, geographical districution, providing valuable insights for strategic decision making and market efforts.")   
    st.table(df.head())

elif selected_input == 'Analysis':
    
    with col4:
        fig = px.bar(df, x = "Retailer", y = "TotalSales", labels={"TotalSales" : "Total Sales {$}"},
                  title = "Total Sales by Retailer",
                  hover_data=["TotalSales"], template="gridon",height=500)
        st.plotly_chart(fig,use_container_width=True)
        df["Month_Year"] = df["InvoiceDate"].dt.strftime("%b'%y")
        result = df.groupby(by = df["Month_Year"])["TotalSales"].sum().reset_index()
    with col5:
        fig1 = px.line(result, x = "Month_Year", y = "TotalSales", title="Total Sales Over Time",
                   template="gridon")
        st.plotly_chart(fig1,use_container_width=True)
        st.divider()
    col6,col7,col8=st.columns([0.1,0.45,0.45])
    with col7: 
        st.subheader("Pie chart of Sales Method")
        fig2,ax1=plt.subplots()
        ax1.pie(x=df['SalesMethod'].value_counts().values,labels=df['SalesMethod'].value_counts().index,autopct="%0.2f%%" )
        st.pyplot(fig=fig2)
    with col8:
        st.subheader("Count plot of Regions")
        fig3=px.bar(data_frame=df,x=df['Region'].value_counts().index,y=df['Region'].value_counts().values)
       
        
        st.plotly_chart(fig3,use_container_width=True)


