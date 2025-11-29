# 🎬 Project 3: Netflix Content Analysis

## 📋 Project Overview

Netflix Movies & TV Shows dataset ka comprehensive statistical analysis - GroupBy operations, aggregations, correlations, aur content insights.

---

## 📊 Dataset Information

| Feature | Description |
|---------|-------------|
| **show_id** | Unique ID for each show |
| **type** | Movie or TV Show |
| **title** | Title of the content |
| **director** | Director name |
| **cast** | Cast members |
| **country** | Country of production |
| **date_added** | Date added to Netflix |
| **release_year** | Year of release |
| **rating** | Content rating (PG, TV-MA, etc.) |
| **duration** | Duration (minutes/seasons) |
| **listed_in** | Genres/Categories |
| **description** | Content description |

---

## 🐼 Pandas Topics Covered (25+ Methods)

### 1️⃣ GroupBy Operations
| Method | Description |
|--------|-------------|
| `groupby()` | Group data for aggregation |
| `agg()` | Multiple aggregations |
| `transform()` | Group-wise transformation |
| `filter()` | Filter groups |
| `apply()` | Apply custom function |

### 2️⃣ Aggregation Functions
| Method | Description |
|--------|-------------|
| `count()` | Count non-null values |
| `sum()` | Sum of values |
| `mean()` | Average |
| `median()` | Median value |
| `std()` | Standard deviation |
| `var()` | Variance |
| `min()` / `max()` | Min/Max values |
| `first()` / `last()` | First/Last values |

### 3️⃣ Statistical Analysis
| Method | Description |
|--------|-------------|
| `describe()` | Statistical summary |
| `corr()` | Correlation matrix |
| `value_counts()` | Frequency counts |
| `quantile()` | Calculate quantiles |
| `rank()` | Rank values |
| `nlargest()` | Top N values |
| `nsmallest()` | Bottom N values |

### 4️⃣ Index Operations
| Method | Description |
|--------|-------------|
| `idxmax()` | Index of maximum |
| `idxmin()` | Index of minimum |
| `reset_index()` | Reset index |
| `set_index()` | Set column as index |
| `unstack()` | Pivot index to columns |

### 5️⃣ String Operations
| Method | Description |
|--------|-------------|
| `str.split()` | Split strings |
| `str.len()` | String length |
| `str.contains()` | Check pattern |
| `str.count()` | Count occurrences |

---

## 📁 Project Files

```
project_3_netflix/
├── README.md               # This documentation
├── netflix_analysis.ipynb  # Jupyter Notebook
├── netflix_analysis.py     # Python script
├── netflix_app.py          # Streamlit Dashboard
└── requirements.txt        # Dependencies
```

---

## 🚀 How to Run

```bash
# Jupyter Notebook
jupyter notebook netflix_analysis.ipynb

# Python Script
python netflix_analysis.py

# Streamlit Dashboard
streamlit run netflix_app.py
```

---

## 🎯 Learning Outcomes

- ✅ Master GroupBy operations
- ✅ Multiple aggregation techniques
- ✅ Statistical analysis methods
- ✅ Content trend analysis
- ✅ Genre distribution insights
- ✅ Country-wise analysis

---

## 👨‍💻 Author

Portfolio Project - Pandas Mastery Series
