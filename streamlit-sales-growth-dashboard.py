import streamlit as st
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

# Streamlit app layout
st.title("Sales Dashboard")
    

def main():
    st.title("Exploratory Data Analysis Dashboard")
    
    df = pd.read_csv("Sales_growth.csv")
    # df = load_data(df)
    df['period'] = pd.to_datetime(df['period'])
    df.drop(["Unnamed: 0"],axis=1,inplace=True)
    st.subheader("Data Overview")
    st.dataframe(df)
    
    # Descriptive statistics
    st.subheader("Descriptive Statistics")
    st.write(df.describe())
    
    # Sales Over Time
    st.subheader("Total Sales Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x='period', y='total_sales', hue='product_category', marker='o', ax=ax)
    plt.title('Total Sales Over Time by Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Sales Growth Analysis
    st.subheader("Sales Growth Analysis")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x='period', y='sales_growth', hue='product_category', ax=ax)
    plt.title('Sales Growth Over Time by Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Correlation Matrix
    # Correlation Matr
    # ix
    st.subheader("Correlation Matrix")
    numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
    correlation_matrix = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    plt.title('Correlation Matrix')
    st.pyplot(fig)

    # Pairplot
    st.subheader("Pairplot of Sales Data")
    
    # Create the pairplot using a temporary figure
    pairplot_fig = sns.pairplot(df, hue='product_category')
    
    # Save the pairplot to a figure
    st.pyplot(pairplot_fig.fig)
    
    # User Input for Prediction (Optional)
    st.sidebar.header("User Input for Prediction")
    selected_category = st.sidebar.selectbox("Select Product Category", df['product_category'].unique())
    
    st.subheader(f"Sales Data for {selected_category}")
    filtered_data = df[df['product_category'] == selected_category]
    st.line_chart(filtered_data.set_index('period')['total_sales'])
    
if __name__ == "__main__":
    main()