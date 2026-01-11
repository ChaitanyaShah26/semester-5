import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Dashboard")

file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)
    
    # Cleaning
    st.header("Cleaning")
    if st.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()
    if st.checkbox("Fill Missing"):
        df = df.fillna(0)
    
    # Preview
    st.header("Data Preview")
    st.dataframe(df)
    
    # Stats
    st.header("Statistics")
    st.write(df.describe())
    
    # Missing
    st.header("Missing Values")
    st.write(df.isnull().sum())
    
    # Columns
    cols = df.columns.tolist()
    
    # Bar
    st.header("Bar Chart")
    st.plotly_chart(px.bar(df, x=st.selectbox("X", cols, key="b1"), y=st.selectbox("Y", cols, key="b2")))
    
    # Line
    st.header("Line Chart")
    st.plotly_chart(px.line(df, x=st.selectbox("X", cols, key="l1"), y=st.selectbox("Y", cols, key="l2")))
    
    # Scatter
    st.header("Scatter Plot")
    st.plotly_chart(px.scatter(df, x=st.selectbox("X", cols, key="s1"), y=st.selectbox("Y", cols, key="s2")))
    
    # Histogram
    st.header("Histogram")
    st.plotly_chart(px.histogram(df, x=st.selectbox("Column", cols, key="h1")))
    
    # Box
    st.header("Box Plot")
    st.plotly_chart(px.box(df, y=st.selectbox("Column", cols, key="bx")))
    
    # Pie
    st.header("Pie Chart")
    st.plotly_chart(px.pie(df, names=st.selectbox("Column", cols, key="p1")))
    
    # Heatmap
    st.header("Correlation Heatmap")
    st.plotly_chart(px.imshow(df.select_dtypes(include='number').corr(), text_auto=True))