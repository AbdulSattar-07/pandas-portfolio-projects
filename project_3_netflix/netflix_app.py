"""
🎬 Netflix Content Analysis Dashboard
======================================
Interactive Statistical Analysis
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
    page_title="🎬 Netflix Analysis",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #141414 0%, #1a1a2e 100%); }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(229, 9, 20, 0.5); }
        50% { box-shadow: 0 0 40px rgba(229, 9, 20, 0.8); }
    }
    
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #E50914;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        animation: glow 2s ease-in-out infinite;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #E50914;
    }
    
    .metric-value { font-size: 2.2rem; font-weight: bold; color: #E50914; }
    .metric-label { color: #aaa; font-size: 0.9rem; margin-top: 5px; }
    
    .movie-card { border-left: 4px solid #E50914; }
    .tv-card { border-left: 4px solid #46d369; }
    
    .section-title {
        font-size: 1.6rem;
        color: #E50914;
        margin: 25px 0 15px 0;
        border-bottom: 2px solid #E50914;
        padding-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    df = pd.read_csv('../netflix_titles.csv')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

df = load_data()

# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="main-title">🎬 NETFLIX</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888; font-size:1.2rem;">Content Analysis Dashboard | GroupBy & Statistics | 25+ Pandas Methods</p>', unsafe_allow_html=True)
st.markdown("---")

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🎛️ Filters")
    
    # Type filter
    type_filter = st.multiselect(
        "📺 Content Type",
        options=df['type'].unique(),
        default=df['type'].unique()
    )
    
    # Year range
    year_min, year_max = st.slider(
        "📅 Release Year",
        min_value=int(df['release_year'].min()),
        max_value=int(df['release_year'].max()),
        value=(2000, 2021)
    )
    
    # Rating filter
    ratings = df['rating'].dropna().unique().tolist()
    rating_filter = st.multiselect(
        "⭐ Rating",
        options=ratings,
        default=ratings[:5]
    )
    
    st.markdown("---")
    st.markdown("### 🐼 GroupBy Methods")
    st.success("groupby(), agg(), transform()\nfilter(), apply()\ncount(), mean(), sum()\nmin(), max(), std()")

# Apply filters
filtered_df = df[
    (df['type'].isin(type_filter)) &
    (df['release_year'].between(year_min, year_max)) &
    (df['rating'].isin(rating_filter) | df['rating'].isna())
]

# ============================================================
# KEY METRICS
# ============================================================
st.markdown('<h2 class="section-title">📈 Key Metrics</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(filtered_df):,}</div>
        <div class="metric-label">Total Titles</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    movies = len(filtered_df[filtered_df['type'] == 'Movie'])
    st.markdown(f"""
    <div class="metric-card movie-card">
        <div class="metric-value">{movies:,}</div>
        <div class="metric-label">Movies</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
    st.markdown(f"""
    <div class="metric-card tv-card">
        <div class="metric-value" style="color:#46d369;">{tv_shows:,}</div>
        <div class="metric-label">TV Shows</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    countries = filtered_df['country'].nunique()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{countries}</div>
        <div class="metric-label">Countries</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# CONTENT DISTRIBUTION
# ============================================================
st.markdown('<h2 class="section-title">📊 Content Distribution</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Type distribution pie
    type_counts = filtered_df['type'].value_counts()
    fig_type = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        title='🎬 Movies vs TV Shows',
        color_discrete_sequence=['#E50914', '#46d369'],
        hole=0.4
    )
    fig_type.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_type, use_container_width=True)

with col2:
    # Rating distribution
    rating_counts = filtered_df['rating'].value_counts().head(10)
    fig_rating = px.bar(
        x=rating_counts.index,
        y=rating_counts.values,
        title='⭐ Top 10 Ratings',
        color=rating_counts.values,
        color_continuous_scale='Reds'
    )
    fig_rating.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis_title='Rating',
        yaxis_title='Count'
    )
    st.plotly_chart(fig_rating, use_container_width=True)

# ============================================================
# YEARLY TRENDS
# ============================================================
st.markdown('<h2 class="section-title">📅 Content Trends</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Content by release year
    yearly = filtered_df.groupby(['release_year', 'type']).size().reset_index(name='count')
    fig_yearly = px.line(
        yearly,
        x='release_year',
        y='count',
        color='type',
        title='📈 Content by Release Year',
        color_discrete_map={'Movie': '#E50914', 'TV Show': '#46d369'}
    )
    fig_yearly.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_yearly, use_container_width=True)

with col2:
    # Content added to Netflix
    added = filtered_df.groupby('year_added').size().reset_index(name='count')
    added = added.dropna()
    fig_added = px.bar(
        added,
        x='year_added',
        y='count',
        title='📥 Content Added to Netflix by Year',
        color='count',
        color_continuous_scale='Reds'
    )
    fig_added.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_added, use_container_width=True)

# ============================================================
# TOP COUNTRIES & GENRES
# ============================================================
st.markdown('<h2 class="section-title">🌍 Geographic & Genre Analysis</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Top countries
    countries_series = filtered_df['country'].dropna().str.split(', ').explode()
    top_countries = countries_series.value_counts().head(10)
    fig_countries = px.bar(
        y=top_countries.index,
        x=top_countries.values,
        orientation='h',
        title='🌍 Top 10 Countries',
        color=top_countries.values,
        color_continuous_scale='Reds'
    )
    fig_countries.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis={'categoryorder': 'total ascending'}
    )
    st.plotly_chart(fig_countries, use_container_width=True)

with col2:
    # Top genres
    genres = filtered_df['listed_in'].str.split(', ').explode()
    top_genres = genres.value_counts().head(10)
    fig_genres = px.bar(
        y=top_genres.index,
        x=top_genres.values,
        orientation='h',
        title='🎭 Top 10 Genres',
        color=top_genres.values,
        color_continuous_scale='Greens'
    )
    fig_genres.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis={'categoryorder': 'total ascending'}
    )
    st.plotly_chart(fig_genres, use_container_width=True)

# ============================================================
# GROUPBY STATISTICS TABLE
# ============================================================
st.markdown('<h2 class="section-title">📊 GroupBy Statistics</h2>', unsafe_allow_html=True)

# GroupBy aggregation showcase
stats = filtered_df.groupby('type').agg(
    Total=('show_id', 'count'),
    Avg_Year=('release_year', 'mean'),
    Min_Year=('release_year', 'min'),
    Max_Year=('release_year', 'max'),
    Std_Year=('release_year', 'std'),
    Countries=('country', 'nunique'),
    Directors=('director', 'nunique')
).round(2)

st.dataframe(stats, use_container_width=True)

# ============================================================
# DATA EXPLORER
# ============================================================
st.markdown('<h2 class="section-title">🔍 Data Explorer</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📋 Browse Content", "📊 Statistics", "🔥 Top Content"])

with tab1:
    st.dataframe(
        filtered_df[['title', 'type', 'rating', 'release_year', 'country', 'listed_in']].head(100),
        use_container_width=True,
        height=400
    )

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### describe() Output")
        st.dataframe(filtered_df.describe().round(2), use_container_width=True)
    with col2:
        st.markdown("### value_counts() - Ratings")
        st.dataframe(filtered_df['rating'].value_counts(), use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🆕 Newest Releases (nlargest)")
        st.dataframe(
            filtered_df.nlargest(10, 'release_year')[['title', 'type', 'release_year']],
            use_container_width=True
        )
    with col2:
        st.markdown("### 📜 Oldest Releases (nsmallest)")
        st.dataframe(
            filtered_df.nsmallest(10, 'release_year')[['title', 'type', 'release_year']],
            use_container_width=True
        )

# ============================================================
# PANDAS METHODS SHOWCASE
# ============================================================
st.markdown('<h2 class="section-title">🐼 Pandas Methods Used</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 GroupBy")
    st.code("""
df.groupby('type').size()
df.groupby('type').count()
df.groupby('type').mean()
df.groupby('type').sum()
df.groupby('type').min()
df.groupby('type').max()
df.groupby('type').std()
df.groupby('type').median()
    """, language='python')

with col2:
    st.markdown("### 🎯 Advanced GroupBy")
    st.code("""
df.groupby('type').agg({
    'col1': 'count',
    'col2': ['mean', 'min']
})
df.groupby('type').transform()
df.groupby('type').filter()
df.groupby('type').apply()
    """, language='python')

with col3:
    st.markdown("### 📈 Statistics")
    st.code("""
df.describe()
df.value_counts()
df.quantile([0.25, 0.5])
df.rank()
df.nlargest(5, 'col')
df.nsmallest(5, 'col')
df.idxmax()
df.idxmin()
    """, language='python')

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #888;">
    <h3 style="color: #E50914;">🎬 Netflix Content Analysis</h3>
    <p>Built with ❤️ using Streamlit & Pandas</p>
    <p>📊 25+ Pandas Methods | GroupBy & Statistics | Portfolio Project</p>
</div>
""", unsafe_allow_html=True)
