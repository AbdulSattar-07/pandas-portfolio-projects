"""
Retail Sales Analytics Dashboard
Interactive Streamlit application for retail sales analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(file):
    """Load and cache data"""
    try:
        df = pd.read_csv(file)
        
        # Convert date and time
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Month_Name'] = df['Date'].dt.month_name()
        df['Day'] = df['Date'].dt.day
        df['DayOfWeek'] = df['Date'].dt.day_name()
        
        if 'Time' in df.columns:
            df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time
            df['Hour'] = pd.to_datetime(df['Time'].astype(str)).dt.hour
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    """Main application"""
    
    # Header
    st.markdown('<h1 class="main-header">🛒 Retail Sales Analytics Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("📊 Navigation")
    
    # File uploader
    uploaded_file = st.sidebar.file_uploader(
        "Upload Supermarket Sales CSV",
        type=['csv'],
        help="Upload the supermarket_sales.csv file"
    )
    
    if uploaded_file is None:
        st.info("👈 Please upload the supermarket sales dataset to begin analysis")
        st.markdown("""
        ### 📥 Dataset Information
        
        **Download from**: [Kaggle - Supermarket Sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)
        
        **Expected columns**:
        - Invoice ID
        - Branch
        - City
        - Customer type
        - Gender
        - Product line
        - Unit price
        - Quantity
        - Tax 5%
        - Total
        - Date
        - Time
        - Payment
        - cogs
        - gross margin percentage
        - gross income
        - Rating
        """)
        return
    
    # Load data
    df = load_data(uploaded_file)
    
    if df is None:
        return
    
    # Sidebar filters
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filters")
    
    # Date range filter
    if 'Date' in df.columns:
        date_range = st.sidebar.date_input(
            "Select Date Range",
            value=(df['Date'].min(), df['Date'].max()),
            min_value=df['Date'].min().date(),
            max_value=df['Date'].max().date()
        )
        
        if len(date_range) == 2:
            df = df[(df['Date'].dt.date >= date_range[0]) & (df['Date'].dt.date <= date_range[1])]
    
    # Product line filter
    if 'Product line' in df.columns:
        product_lines = st.sidebar.multiselect(
            "Select Product Lines",
            options=df['Product line'].unique(),
            default=df['Product line'].unique()
        )
        df = df[df['Product line'].isin(product_lines)]
    
    # Branch filter
    if 'Branch' in df.columns:
        branches = st.sidebar.multiselect(
            "Select Branches",
            options=df['Branch'].unique(),
            default=df['Branch'].unique()
        )
        df = df[df['Branch'].isin(branches)]
    
    # Navigation
    page = st.sidebar.radio(
        "Select Analysis",
        ["📊 Overview", "📦 Product Analysis", "📅 Time Series", "👥 Customer Analysis", "🔗 Correlations", "📋 Raw Data"]
    )
    
    # Display selected page
    if page == "📊 Overview":
        show_overview(df)
    elif page == "📦 Product Analysis":
        show_product_analysis(df)
    elif page == "📅 Time Series":
        show_time_series(df)
    elif page == "👥 Customer Analysis":
        show_customer_analysis(df)
    elif page == "🔗 Correlations":
        show_correlations(df)
    elif page == "📋 Raw Data":
        show_raw_data(df)

def show_overview(df):
    """Display overview metrics"""
    st.header("📊 Business Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = df['Total'].sum()
        st.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
    
    with col2:
        avg_transaction = df['Total'].mean()
        st.metric("💵 Avg Transaction", f"${avg_transaction:.2f}")
    
    with col3:
        total_transactions = len(df)
        st.metric("🛒 Total Transactions", f"{total_transactions:,}")
    
    with col4:
        if 'Rating' in df.columns:
            avg_rating = df['Rating'].mean()
            st.metric("⭐ Avg Rating", f"{avg_rating:.2f}/10")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Product line' in df.columns:
            st.subheader("🏆 Top Products by Revenue")
            product_revenue = df.groupby('Product line')['Total'].sum().sort_values(ascending=True)
            fig = px.bar(
                x=product_revenue.values,
                y=product_revenue.index,
                orientation='h',
                labels={'x': 'Revenue ($)', 'y': 'Product Line'},
                color=product_revenue.values,
                color_continuous_scale='Blues'
            )
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'Branch' in df.columns:
            st.subheader("🏢 Revenue by Branch")
            branch_revenue = df.groupby('Branch')['Total'].sum()
            fig = px.pie(
                values=branch_revenue.values,
                names=branch_revenue.index,
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Daily trend
    if 'Date' in df.columns:
        st.subheader("📈 Daily Sales Trend")
        daily_sales = df.groupby('Date')['Total'].sum().reset_index()
        fig = px.line(
            daily_sales,
            x='Date',
            y='Total',
            labels={'Total': 'Revenue ($)', 'Date': 'Date'},
            markers=True
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_product_analysis(df):
    """Display product analysis"""
    st.header("📦 Product Analysis")
    
    if 'Product line' not in df.columns:
        st.warning("Product line column not found in dataset")
        return
    
    # Product performance table
    st.subheader("📊 Product Performance Metrics")
    product_stats = df.groupby('Product line').agg({
        'Total': ['sum', 'mean', 'count'],
        'Quantity': 'sum',
        'Rating': 'mean'
    }).round(2)
    product_stats.columns = ['Total Revenue', 'Avg Sale', 'Transactions', 'Units Sold', 'Avg Rating']
    product_stats = product_stats.sort_values('Total Revenue', ascending=False)
    st.dataframe(product_stats, use_container_width=True)
    
    # Profit analysis
    if 'gross income' in df.columns:
        st.subheader("💰 Profit Analysis")
        profit_data = df.groupby('Product line').agg({
            'Total': 'sum',
            'cogs': 'sum',
            'gross income': 'sum'
        })
        profit_data['Profit Margin %'] = (profit_data['gross income'] / profit_data['Total'] * 100).round(2)
        profit_data = profit_data.sort_values('gross income', ascending=False)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Revenue',
            x=profit_data.index,
            y=profit_data['Total'],
            marker_color='lightblue'
        ))
        fig.add_trace(go.Bar(
            name='Cost',
            x=profit_data.index,
            y=profit_data['cogs'],
            marker_color='lightcoral'
        ))
        fig.add_trace(go.Bar(
            name='Profit',
            x=profit_data.index,
            y=profit_data['gross income'],
            marker_color='lightgreen'
        ))
        fig.update_layout(
            barmode='group',
            xaxis_title='Product Line',
            yaxis_title='Amount ($)',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Product comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Quantity Sold")
        qty_data = df.groupby('Product line')['Quantity'].sum().sort_values(ascending=True)
        fig = px.bar(
            x=qty_data.values,
            y=qty_data.index,
            orientation='h',
            labels={'x': 'Units Sold', 'y': 'Product Line'},
            color=qty_data.values,
            color_continuous_scale='Greens'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("⭐ Average Rating")
        rating_data = df.groupby('Product line')['Rating'].mean().sort_values(ascending=True)
        fig = px.bar(
            x=rating_data.values,
            y=rating_data.index,
            orientation='h',
            labels={'x': 'Average Rating', 'y': 'Product Line'},
            color=rating_data.values,
            color_continuous_scale='Oranges'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_time_series(df):
    """Display time series analysis"""
    st.header("📅 Time Series Analysis")
    
    if 'Date' not in df.columns:
        st.warning("Date column not found in dataset")
        return
    
    # Monthly analysis
    st.subheader("📆 Monthly Performance")
    monthly_data = df.groupby('Month_Name').agg({
        'Total': ['sum', 'mean', 'count']
    }).round(2)
    monthly_data.columns = ['Total Revenue', 'Avg Transaction', 'Transaction Count']
    st.dataframe(monthly_data, use_container_width=True)
    
    # Monthly trend
    monthly_revenue = df.groupby('Month')['Total'].sum().reset_index()
    fig = px.bar(
        monthly_revenue,
        x='Month',
        y='Total',
        labels={'Total': 'Revenue ($)', 'Month': 'Month'},
        color='Total',
        color_continuous_scale='Blues'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Day of week analysis
    if 'DayOfWeek' in df.columns:
        st.subheader("📊 Sales by Day of Week")
        dow_data = df.groupby('DayOfWeek')['Total'].sum().reindex([
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])
        fig = px.bar(
            x=dow_data.index,
            y=dow_data.values,
            labels={'x': 'Day of Week', 'y': 'Revenue ($)'},
            color=dow_data.values,
            color_continuous_scale='Viridis'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Hourly analysis
    if 'Hour' in df.columns:
        st.subheader("🕐 Sales by Hour")
        hourly_data = df.groupby('Hour')['Total'].sum()
        fig = px.line(
            x=hourly_data.index,
            y=hourly_data.values,
            labels={'x': 'Hour of Day', 'y': 'Revenue ($)'},
            markers=True
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_customer_analysis(df):
    """Display customer analysis"""
    st.header("👥 Customer Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Customer type' in df.columns:
            st.subheader("👤 Customer Type")
            customer_data = df.groupby('Customer type').agg({
                'Total': ['sum', 'mean', 'count']
            }).round(2)
            customer_data.columns = ['Total Revenue', 'Avg Purchase', 'Transactions']
            st.dataframe(customer_data, use_container_width=True)
            
            # Pie chart
            fig = px.pie(
                values=customer_data['Total Revenue'],
                names=customer_data.index,
                title='Revenue by Customer Type',
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'Gender' in df.columns:
            st.subheader("⚧ Gender Analysis")
            gender_data = df.groupby('Gender').agg({
                'Total': ['sum', 'mean', 'count']
            }).round(2)
            gender_data.columns = ['Total Revenue', 'Avg Purchase', 'Transactions']
            st.dataframe(gender_data, use_container_width=True)
            
            # Pie chart
            fig = px.pie(
                values=gender_data['Total Revenue'],
                names=gender_data.index,
                title='Revenue by Gender',
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Payment method analysis
    if 'Payment' in df.columns:
        st.subheader("💳 Payment Method Analysis")
        payment_data = df.groupby('Payment')['Total'].agg(['sum', 'count']).round(2)
        payment_data.columns = ['Total Revenue', 'Transaction Count']
        
        fig = px.bar(
            payment_data,
            x=payment_data.index,
            y='Total Revenue',
            labels={'x': 'Payment Method', 'Total Revenue': 'Revenue ($)'},
            color='Total Revenue',
            color_continuous_scale='Purples'
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Rating distribution
    if 'Rating' in df.columns:
        st.subheader("⭐ Rating Distribution")
        fig = px.histogram(
            df,
            x='Rating',
            nbins=20,
            labels={'Rating': 'Rating', 'count': 'Frequency'},
            color_discrete_sequence=['skyblue']
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_correlations(df):
    """Display correlation analysis"""
    st.header("🔗 Correlation Analysis")
    
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Remove date-related columns
    numerical_cols = [col for col in numerical_cols if col not in ['Year', 'Month', 'Day', 'Hour']]
    
    if len(numerical_cols) < 2:
        st.warning("Not enough numerical columns for correlation analysis")
        return
    
    # Correlation matrix
    corr_matrix = df[numerical_cols].corr()
    
    # Heatmap
    fig = px.imshow(
        corr_matrix,
        labels=dict(color="Correlation"),
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        color_continuous_scale='RdBu_r',
        zmin=-1,
        zmax=1,
        text_auto='.2f'
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Strong correlations
    st.subheader("🔗 Strong Correlations (|r| > 0.7)")
    strong_corr = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > 0.7:
                strong_corr.append({
                    'Variable 1': corr_matrix.columns[i],
                    'Variable 2': corr_matrix.columns[j],
                    'Correlation': round(corr_matrix.iloc[i, j], 3)
                })
    
    if strong_corr:
        st.dataframe(pd.DataFrame(strong_corr), use_container_width=True)
    else:
        st.info("No strong correlations found (|r| > 0.7)")

def show_raw_data(df):
    """Display raw data"""
    st.header("📋 Raw Data")
    
    st.subheader("📊 Dataset Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", f"{df.shape[0]:,}")
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Memory", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    st.subheader("🔍 Data Preview")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name='filtered_sales_data.csv',
        mime='text/csv'
    )

if __name__ == "__main__":
    main()
