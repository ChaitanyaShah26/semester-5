import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# 1. PAGE SETUP
st.set_page_config(page_title="Auto-Analytics Dashboard", layout="wide")
st.title("🚀 Automated Data Analytics & Visualization")

# 2. FILE UPLOAD (Main Screen)
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Load Data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # --- COMPULSORY AUTO-PROCESSING (Cleaning & Encoding) ---
    # A. Remove Duplicates
    df.drop_duplicates(inplace=True)

    # B. Handle Missing Values (Mean for numeric, Mode for categorical)
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].mean())

    # C. Auto-Encoding (Label Encoding for all categorical columns)
    # We store a copy for visualization names, but the main df gets encoded
    label_encoders = {}
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le 

    st.success("✅ Data Auto-Cleaned and Encoded Successfully!")

    # 3. DATA STATISTICS (EDA)
    st.header("📋 Automated Data Statistics")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Data Preview (Processed)")
        st.write(df.head())
        st.write(f"**Shape:** {df.shape[0]} rows | {df.shape[1]} columns")
    
    with col_b:
        st.subheader("Statistical Summary")
        st.write(df.describe())

    # 4. DATA VISUALIZATION
    st.markdown("---")
    st.header("🎨 Interactive Visualizations")
    
    # Selecting Plot Type
    plot_option = st.selectbox("Choose a Plot Type", [
        "Bar Chart", "Line Chart", "Scatter Plot", "Histogram", 
        "Box Plot", "Violin Plot", "Pie Chart", "Area Chart", 
        "Correlation Heatmap", "Density Contour"
    ])

    all_cols = df.columns.tolist()
    num_cols = df.select_dtypes(exclude=['object']).columns.tolist()

    try:
        if plot_option == "Bar Chart":
            x, y = st.columns(2)
            xc = x.selectbox("X Axis", all_cols)
            yc = y.selectbox("Y Axis", num_cols)
            fig = px.bar(df, x=xc, y=yc, color=xc, template="plotly_white")

        elif plot_option == "Line Chart":
            x, y = st.columns(2)
            xc = x.selectbox("X Axis", all_cols)
            yc = y.selectbox("Y Axis", num_cols)
            fig = px.line(df, x=xc, y=yc, markers=True)

        elif plot_option == "Scatter Plot":
            x, y, color = st.columns(3)
            xc = x.selectbox("X Axis", num_cols)
            yc = y.selectbox("Y Axis", num_cols)
            cc = color.selectbox("Color By", [None] + all_cols)
            fig = px.scatter(df, x=xc, y=yc, color=cc)

        elif plot_option == "Histogram":
            col = st.selectbox("Select Column", all_cols)
            fig = px.histogram(df, x=col, nbins=30, marginal="box")

        elif plot_option == "Box Plot":
            x, y = st.columns(2)
            xc = x.selectbox("Category", all_cols)
            yc = y.selectbox("Value", num_cols)
            fig = px.box(df, x=xc, y=yc, color=xc)

        elif plot_option == "Violin Plot":
            x, y = st.columns(2)
            xc = x.selectbox("Category", all_cols)
            yc = y.selectbox("Value", num_cols)
            fig = px.violin(df, x=xc, y=yc, box=True, points="all")

        elif plot_option == "Pie Chart":
            names = st.selectbox("Names (Category)", all_cols)
            values = st.selectbox("Values (Numeric)", num_cols)
            fig = px.pie(df, names=names, values=values)

        elif plot_option == "Area Chart":
            x, y = st.columns(2)
            xc = x.selectbox("X Axis", all_cols)
            yc = y.selectbox("Y Axis", num_cols)
            fig = px.area(df, x=xc, y=yc)

        elif plot_option == "Correlation Heatmap":
            corr = df.corr()
            fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')

        elif plot_option == "Density Contour":
            x, y = st.columns(2)
            xc = x.selectbox("X Axis", num_cols)
            yc = y.selectbox("Y Axis", num_cols)
            fig = px.density_contour(df, x=xc, y=yc)

        # Show Plot
        st.plotly_chart(fig, use_container_width=True)
ś
    except Exception as e:
        st.warning(f"Select appropriate columns for the {plot_option}. (Error: {e})")

else:
    st.info("💡 Please upload a dataset to start the automated analysis.")