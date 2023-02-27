import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
st.header(" :red[My First Data App using Streamlit 🥂🍻🥂]")

st.title(":blue[Credit Card Spending Habits in India]")
st.text(" -- Based on Gender, Location, and Transaction Trends ")
img = image.imread('credit img.jpg')
st.image(img)

st.header(':green[About Dataset :]')
st.write("This dataset contains insights into credit card transactions made in India, offering a comprehensive look at the spending habits of Indians across the nation") 
st.subheader('Attribute Information')
st.text('* City: The city in which the transaction took place. (String)')
st.text('* Date: The date of the transaction. (Date)')
st.text('* Card Type: The type of credit card used for the transaction. (String)')
st.text('* Exp Type: The type of expense associated with the transaction. (String)')
st.text('* Gender: The gender of the cardholder. (String)')
st.text('* Amount: The amount of the transaction. (Number)')
st.header(":green[Problem Statement :]")
st.write('To analyze consumer trends and interests by looking at the type of purchases people make based on their gender and city.')
    
st.header(":green[Overview of Dataset]")
df = pd.read_csv('Credit card transactions - India - Simple.csv')
df = df.drop(columns='index')

status = st.radio("Click to know more : ", ('View Dataset','Shape', 'Attributes','Summary','Descriptive statistics' ))

if (status == 'View Dataset'):
    st.dataframe(df.head(10))
elif (status == 'Shape'):
    rows = df.count()[0]
    columns = df.shape[1] - 1
    st.text(f'Number of Rows in the data are : {rows}')
    st.text(f' Number of Columns in the data are : {columns}')
elif (status == 'Attributes'):
    st.write('* City')
    st.write('* Date')
    st.write('* Card Type')
    st.write('* Exp Type')
    st.write('* Gender')
    st.write('* Amount')       
elif (status == 'Summary'):
    img = image.imread('info.jpg')
    st.image(img)    
else:       
    x = df.describe(include = "object")
    st.table(x)
    y = df.describe()
    st.table(y)



def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

creditcard = convert_df(df)

st.download_button(
    label="Download Dataset",
    data = creditcard ,
    file_name='Credit_card transactions_India.csv',
    mime='text/csv',
)




