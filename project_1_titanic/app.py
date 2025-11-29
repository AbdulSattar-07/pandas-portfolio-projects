"""
🚢 Titanic Survival Analysis - Interactive Dashboard
====================================================
Professional Streamlit UI with Animations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="🚢 Titanic Analysis",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS FOR ANIMATIONS & STYLING
# ============================================================
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Animated title */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d4ff, #7b2cbf, #ff006e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInDown 1s ease-out;
        margin-bottom: 0;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        animation: fadeInDown 1.2s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# More CSS
st.markdown("""
<style>
    /* Metric cards */
    .metric-card {
        background: linear-gradient(145deg, #1e3a5f, #0d1b2a);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0,212,255,0.2);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00d4ff;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #aaa;
        margin-top: 5px;
    }
    
    /* Survival cards */
    .survived-card {
        background: linear-gradient(145deg, #0a4d3c, #063829);
        border-left: 4px solid #00ff88;
    }
    
    .died-card {
        background: linear-gradient(145deg, #4d0a1a, #380613);
        border-left: 4px solid #ff4466;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        color: #00d4ff;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #00d4ff;
    }
    
    /* Data table styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f0f1a 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    df = pd.read_csv('../Titanic-Dataset.csv')
    return df

df = load_data()

# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="main-title">🚢 Titanic Survival Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Interactive Dashboard | 25+ Pandas Methods | Portfolio Project</p>', unsafe_allow_html=True)
st.markdown("---")

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🎛️ Controls")
    
    # Gender filter
    gender_filter = st.multiselect(
        "👤 Select Gender",
        options=df['Sex'].unique(),
        default=df['Sex'].unique()
    )
    
    # Class filter
    class_filter = st.multiselect(
        "🎫 Select Class",
        options=sorted(df['Pclass'].unique()),
        default=sorted(df['Pclass'].unique())
    )
    
    # Age range
    age_min, age_max = st.slider(
        "📅 Age Range",
        min_value=int(df['Age'].min()),
        max_value=int(df['Age'].max()),
        value=(0, 80)
    )
    
    st.markdown("---")
    st.markdown("### 📊 Dataset Info")
    st.info(f"**Rows:** {df.shape[0]}\n\n**Columns:** {df.shape[1]}")
    
    st.markdown("---")
    st.markdown("### 🐼 Pandas Methods Used")
    st.success("25+ methods covered including:\n- read_csv, head, tail\n- info, describe, shape\n- loc, iloc, query\n- groupby, agg\n- value_counts, unique")

# Apply filters
filtered_df = df[
    (df['Sex'].isin(gender_filter)) &
    (df['Pclass'].isin(class_filter)) &
    (df['Age'].between(age_min, age_max, inclusive='both') | df['Age'].isna())
]

# ============================================================
# KEY METRICS ROW
# ============================================================
st.markdown('<h2 class="section-header">📈 Key Metrics</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(filtered_df)}</div>
        <div class="metric-label">Total Passengers</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    survival_rate = filtered_df['Survived'].mean() * 100
    st.markdown(f"""
    <div class="metric-card survived-card">
        <div class="metric-value" style="color: #00ff88;">{survival_rate:.1f}%</div>
        <div class="metric-label">Survival Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_age = filtered_df['Age'].mean()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{avg_age:.1f}</div>
        <div class="metric-label">Average Age</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_fare = filtered_df['Fare'].mean()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${avg_fare:.0f}</div>
        <div class="metric-label">Average Fare</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SURVIVAL ANALYSIS CHARTS
# ============================================================
st.markdown('<h2 class="section-header">🎯 Survival Analysis</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Survival by Gender
    gender_survival = filtered_df.groupby('Sex')['Survived'].mean().reset_index()
    gender_survival['Survived'] = gender_survival['Survived'] * 100
    
    fig_gender = px.bar(
        gender_survival,
        x='Sex',
        y='Survived',
        color='Sex',
        color_discrete_map={'female': '#ff006e', 'male': '#00d4ff'},
        title='🚻 Survival Rate by Gender',
        labels={'Survived': 'Survival Rate (%)', 'Sex': 'Gender'}
    )
    fig_gender.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    fig_gender.update_traces(marker_line_width=0)
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    # Survival by Class
    class_survival = filtered_df.groupby('Pclass')['Survived'].mean().reset_index()
    class_survival['Survived'] = class_survival['Survived'] * 100
    class_survival['Class'] = class_survival['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
    
    fig_class = px.bar(
        class_survival,
        x='Class',
        y='Survived',
        color='Pclass',
        color_continuous_scale='viridis',
        title='🎫 Survival Rate by Class',
        labels={'Survived': 'Survival Rate (%)', 'Class': 'Passenger Class'}
    )
    fig_class.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    st.plotly_chart(fig_class, use_container_width=True)

# ============================================================
# AGE DISTRIBUTION & PIE CHART
# ============================================================
col1, col2 = st.columns(2)

with col1:
    # Age Distribution
    fig_age = px.histogram(
        filtered_df.dropna(subset=['Age']),
        x='Age',
        color='Survived',
        color_discrete_map={0: '#ff4466', 1: '#00ff88'},
        title='📊 Age Distribution by Survival',
        labels={'Survived': 'Survived', 'Age': 'Age'},
        nbins=30,
        barmode='overlay',
        opacity=0.7
    )
    fig_age.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        legend=dict(title='Survived', orientation='h', y=1.1)
    )
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    # Survival Pie Chart
    survival_counts = filtered_df['Survived'].value_counts()
    fig_pie = px.pie(
        values=survival_counts.values,
        names=['Did Not Survive', 'Survived'],
        title='🥧 Overall Survival Distribution',
        color_discrete_sequence=['#ff4466', '#00ff88'],
        hole=0.4
    )
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# ============================================================
# FARE ANALYSIS
# ============================================================
st.markdown('<h2 class="section-header">💰 Fare Analysis</h2>', unsafe_allow_html=True)

fig_fare = px.box(
    filtered_df,
    x='Pclass',
    y='Fare',
    color='Survived',
    color_discrete_map={0: '#ff4466', 1: '#00ff88'},
    title='💵 Fare Distribution by Class and Survival',
    labels={'Pclass': 'Passenger Class', 'Fare': 'Fare ($)', 'Survived': 'Survived'}
)
fig_fare.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    xaxis=dict(tickmode='array', tickvals=[1, 2, 3], ticktext=['1st Class', '2nd Class', '3rd Class'])
)
st.plotly_chart(fig_fare, use_container_width=True)

# ============================================================
# HEATMAP - SURVIVAL BY SEX & CLASS
# ============================================================
st.markdown('<h2 class="section-header">🔥 Survival Heatmap</h2>', unsafe_allow_html=True)

# Create pivot table using pandas - handle filtered data properly
pivot_data = filtered_df.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack() * 100

# Get actual labels from pivot table (handles filtered data)
if not pivot_data.empty:
    x_labels = [f'{c} Class' if isinstance(c, int) else str(c) for c in pivot_data.columns.tolist()]
    y_labels = [s.capitalize() for s in pivot_data.index.tolist()]
    
    fig_heatmap = px.imshow(
        pivot_data.values,
        x=x_labels,
        y=y_labels,
        color_continuous_scale='RdYlGn',
        title='🗺️ Survival Rate (%) by Gender and Class',
        labels={'color': 'Survival %'},
        text_auto='.1f'
    )
    fig_heatmap.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
else:
    st.warning("No data available for heatmap with current filters.")

# ============================================================
# DATA EXPLORER
# ============================================================
st.markdown('<h2 class="section-header">🔍 Data Explorer</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📋 Raw Data", "📊 Statistics", "❓ Missing Data"])

with tab1:
    st.dataframe(
        filtered_df.style.background_gradient(subset=['Age', 'Fare'], cmap='Blues'),
        use_container_width=True,
        height=400
    )

with tab2:
    st.markdown("### Statistical Summary (describe())")
    st.dataframe(filtered_df.describe().round(2), use_container_width=True)

with tab3:
    st.markdown("### Missing Values (isna().sum())")
    missing = filtered_df.isna().sum()
    missing_pct = (missing / len(filtered_df) * 100).round(2)
    missing_df = pd.DataFrame({
        'Column': missing.index,
        'Missing Count': missing.values,
        'Missing %': missing_pct.values
    })
    st.dataframe(missing_df[missing_df['Missing Count'] > 0], use_container_width=True)

# ============================================================
# PANDAS METHODS SHOWCASE
# ============================================================
st.markdown('<h2 class="section-header">🐼 Pandas Methods Showcase</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📥 Data Loading")
    st.code("""
# 1. read_csv()
df = pd.read_csv('titanic.csv')
    """, language='python')
    
    st.markdown("### 🔍 Inspection")
    st.code("""
# 2-12. Inspection methods
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.size
df.ndim
df.columns
df.index
df.dtypes
df.memory_usage()
    """, language='python')

with col2:
    st.markdown("### 🎯 Selection")
    st.code("""
# 13-17. Selection methods
df.loc[0:5, ['Name', 'Age']]
df.iloc[0:5, 0:3]
df.at[0, 'Name']
df.iat[0, 3]
df.query('Age > 30')
    """, language='python')
    
    st.markdown("### 📊 Analysis")
    st.code("""
# 18-25. Analysis methods
df['Col'].value_counts()
df['Col'].unique()
df['Col'].nunique()
df['Col'].sum()
df['Col'].mean()
df['Col'].median()
df['Col'].min()
df['Col'].max()
    """, language='python')

with col3:
    st.markdown("### 🔧 Manipulation")
    st.code("""
# 26-30. Manipulation
df.sort_values('Age')
df.sort_index()
df.sample(5)
df.copy()
df.rename(columns={...})
    """, language='python')
    
    st.markdown("### 📈 GroupBy")
    st.code("""
# 31-37. GroupBy operations
df.groupby('Sex')['Survived'].mean()
df.groupby('Pclass').agg({
    'Survived': 'mean',
    'Age': 'mean'
})
df.isna().sum()
df.notna()
    """, language='python')

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #888;">
    <h3>🚢 Titanic Survival Analysis Dashboard</h3>
    <p>Built with ❤️ using Streamlit & Pandas</p>
    <p>📊 25+ Pandas Methods Demonstrated | Portfolio Project</p>
    <br>
    <p style="font-size: 0.8rem;">
        Dataset: Titanic - Machine Learning from Disaster | Kaggle
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR FOOTER
# ============================================================
with st.sidebar:
    st.markdown("---")
    st.markdown("""
    ### 📁 Project Files
    - `README.md` - Documentation
    - `titanic_analysis.ipynb` - Jupyter Notebook
    - `titanic_analysis.py` - Python Script
    - `titanic_app.py` - This Dashboard
    """)
    
    st.markdown("---")
    st.markdown("### 🚀 Run Commands")
    st.code("streamlit run titanic_app.py", language='bash')
