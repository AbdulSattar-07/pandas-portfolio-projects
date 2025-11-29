"""
🛒 E-Commerce Data Cleaning Dashboard
======================================
Interactive Data Quality Analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="🛒 E-Commerce Cleaning",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        background: linear-gradient(90deg, #f093fb, #f5576c, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: slideIn 1s ease-out;
    }
    
    .metric-box {
        background: linear-gradient(145deg, #2d2d44, #1a1a2e);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-box:hover { transform: scale(1.05); }
    
    .metric-value { font-size: 2rem; font-weight: bold; color: #4facfe; }
    .metric-label { color: #aaa; font-size: 0.9rem; }
    
    .clean-box { border-left: 4px solid #00ff88; }
    .dirty-box { border-left: 4px solid #ff4466; }
    
    .section-title {
        font-size: 1.5rem;
        color: #f5576c;
        margin: 25px 0 15px 0;
        border-bottom: 2px solid #f5576c;
        padding-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    df = pd.read_csv('../OnlineRetail.csv', encoding='ISO-8859-1')
    return df

@st.cache_data
def clean_data(df):
    df_clean = df.copy()
    # Drop missing CustomerID
    df_clean = df_clean.dropna(subset=['CustomerID'])
    # Fill missing Description
    df_clean['Description'] = df_clean['Description'].fillna('No Description')
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    # Convert types
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    # Add columns
    df_clean['Year'] = df_clean['InvoiceDate'].dt.year
    df_clean['Month'] = df_clean['InvoiceDate'].dt.month
    df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']
    return df_clean

df_original = load_data()
df_clean = clean_data(df_original)

# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="main-title">🛒 E-Commerce Data Cleaning Pipeline</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888;">Interactive Data Quality Dashboard | 20+ Pandas Methods</p>', unsafe_allow_html=True)
st.markdown("---")

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🎛️ Data View")
    view_mode = st.radio("Select Dataset", ["Original Data", "Cleaned Data", "Compare Both"])
    
    st.markdown("---")
    st.markdown("## 📊 Quick Stats")
    st.metric("Original Rows", f"{len(df_original):,}")
    st.metric("Cleaned Rows", f"{len(df_clean):,}")
    st.metric("Rows Removed", f"{len(df_original) - len(df_clean):,}")
    
    st.markdown("---")
    st.markdown("### 🐼 Methods Used")
    st.success("20+ methods:\n- isna, fillna, dropna\n- duplicated, drop_duplicates\n- astype, to_datetime\n- replace, where, mask\n- str.strip, str.upper\n- query, clip, assign")

# ============================================================
# KEY METRICS
# ============================================================
st.markdown('<h2 class="section-title">📈 Data Quality Metrics</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    missing_orig = df_original.isna().sum().sum()
    st.markdown(f"""
    <div class="metric-box dirty-box">
        <div class="metric-value" style="color:#ff4466;">{missing_orig:,}</div>
        <div class="metric-label">Missing Values (Original)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    missing_clean = df_clean.isna().sum().sum()
    st.markdown(f"""
    <div class="metric-box clean-box">
        <div class="metric-value" style="color:#00ff88;">{missing_clean:,}</div>
        <div class="metric-label">Missing Values (Cleaned)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    dups_orig = df_original.duplicated().sum()
    st.markdown(f"""
    <div class="metric-box dirty-box">
        <div class="metric-value" style="color:#ff4466;">{dups_orig:,}</div>
        <div class="metric-label">Duplicates (Original)</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    dups_clean = df_clean.duplicated().sum()
    st.markdown(f"""
    <div class="metric-box clean-box">
        <div class="metric-value" style="color:#00ff88;">{dups_clean:,}</div>
        <div class="metric-label">Duplicates (Cleaned)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# MISSING DATA ANALYSIS
# ============================================================
st.markdown('<h2 class="section-title">❓ Missing Data Analysis</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Missing values bar chart - Original
    missing_orig_df = pd.DataFrame({
        'Column': df_original.columns,
        'Missing': df_original.isna().sum().values,
        'Percentage': (df_original.isna().sum() / len(df_original) * 100).values
    }).sort_values('Missing', ascending=True)
    
    fig_missing = px.bar(
        missing_orig_df[missing_orig_df['Missing'] > 0],
        y='Column', x='Missing',
        orientation='h',
        title='📊 Missing Values (Original)',
        color='Missing',
        color_continuous_scale='Reds'
    )
    fig_missing.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_missing, use_container_width=True)

with col2:
    # Missing values comparison
    comparison_data = pd.DataFrame({
        'Dataset': ['Original', 'Cleaned'],
        'Missing Values': [df_original.isna().sum().sum(), df_clean.isna().sum().sum()],
        'Duplicates': [df_original.duplicated().sum(), df_clean.duplicated().sum()]
    })
    
    fig_compare = px.bar(
        comparison_data,
        x='Dataset',
        y=['Missing Values', 'Duplicates'],
        barmode='group',
        title='📉 Before vs After Cleaning',
        color_discrete_sequence=['#ff4466', '#ffaa00']
    )
    fig_compare.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_compare, use_container_width=True)

# ============================================================
# DATA TYPE ANALYSIS
# ============================================================
st.markdown('<h2 class="section-title">🔄 Data Type Conversion</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Original Data Types")
    dtype_orig = pd.DataFrame({
        'Column': df_original.dtypes.index,
        'Type': df_original.dtypes.values.astype(str)
    })
    st.dataframe(dtype_orig, use_container_width=True, height=300)

with col2:
    st.markdown("### Cleaned Data Types")
    dtype_clean = pd.DataFrame({
        'Column': df_clean.dtypes.index,
        'Type': df_clean.dtypes.values.astype(str)
    })
    st.dataframe(dtype_clean, use_container_width=True, height=300)

# ============================================================
# SALES ANALYSIS (CLEANED DATA)
# ============================================================
st.markdown('<h2 class="section-title">💰 Sales Analysis (Cleaned Data)</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Top countries
    country_sales = df_clean.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
    fig_country = px.bar(
        x=country_sales.values,
        y=country_sales.index,
        orientation='h',
        title='🌍 Top 10 Countries by Sales',
        color=country_sales.values,
        color_continuous_scale='Viridis'
    )
    fig_country.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis={'categoryorder': 'total ascending'}
    )
    st.plotly_chart(fig_country, use_container_width=True)

with col2:
    # Monthly sales
    monthly_sales = df_clean.groupby('Month')['TotalPrice'].sum()
    fig_monthly = px.line(
        x=monthly_sales.index,
        y=monthly_sales.values,
        title='📅 Monthly Sales Trend',
        markers=True
    )
    fig_monthly.update_traces(line_color='#4facfe', marker_color='#f5576c')
    fig_monthly.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis_title='Month',
        yaxis_title='Total Sales'
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

# ============================================================
# DATA EXPLORER
# ============================================================
st.markdown('<h2 class="section-title">🔍 Data Explorer</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📋 Original Data", "✅ Cleaned Data", "📊 Statistics"])

with tab1:
    st.dataframe(df_original.head(100), use_container_width=True, height=400)

with tab2:
    st.dataframe(df_clean.head(100), use_container_width=True, height=400)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Original Statistics")
        st.dataframe(df_original.describe().round(2), use_container_width=True)
    with col2:
        st.markdown("### Cleaned Statistics")
        st.dataframe(df_clean.describe().round(2), use_container_width=True)

# ============================================================
# PANDAS METHODS SHOWCASE
# ============================================================
st.markdown('<h2 class="section-title">🐼 Pandas Methods Showcase</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ❓ Missing Data")
    st.code("""
# Detection
df.isna()
df.isnull()
df.notna()
df.notnull()

# Handling
df.fillna(value)
df.dropna()
df.interpolate()
    """, language='python')

with col2:
    st.markdown("### 🔄 Duplicates & Types")
    st.code("""
# Duplicates
df.duplicated()
df.drop_duplicates()

# Type Conversion
df.astype(int)
pd.to_datetime(df['col'])
pd.to_numeric(df['col'])
    """, language='python')

with col3:
    st.markdown("### 🎯 Filter & Replace")
    st.code("""
# Filtering
df.query('col > 0')
df.where(condition)
df.mask(condition)
df.clip(lower, upper)

# String ops
df['col'].str.strip()
df['col'].str.upper()
df['col'].str.contains()
    """, language='python')

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #888;">
    <h3>🛒 E-Commerce Data Cleaning Pipeline</h3>
    <p>Built with ❤️ using Streamlit & Pandas</p>
    <p>📊 20+ Pandas Methods | Portfolio Project</p>
</div>
""", unsafe_allow_html=True)
