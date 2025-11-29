# 🚢 Project 1: Titanic Survival Analysis

## 📋 Project Overview

Titanic dataset ka comprehensive Exploratory Data Analysis (EDA) using Pandas. Is project mein hum analyze karenge ke kaun passengers survive huay aur kaun nahi - Age, Gender, Class ke basis par.

---

## 📊 Dataset Information

| Feature | Description |
|---------|-------------|
| **PassengerId** | Unique ID for each passenger |
| **Survived** | Survival (0 = No, 1 = Yes) |
| **Pclass** | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| **Name** | Passenger name |
| **Sex** | Gender (male/female) |
| **Age** | Age in years |
| **SibSp** | # of siblings/spouses aboard |
| **Parch** | # of parents/children aboard |
| **Ticket** | Ticket number |
| **Fare** | Passenger fare |
| **Cabin** | Cabin number |
| **Embarked** | Port of Embarkation (C=Cherbourg, Q=Queenstown, S=Southampton) |

---

## 🐼 Pandas Topics Covered (25+ Methods)

### 1️⃣ Data Loading
| Method | Description |
|--------|-------------|
| `pd.read_csv()` | Load CSV file into DataFrame |

### 2️⃣ Data Inspection
| Method | Description |
|--------|-------------|
| `head()` | Display first N rows |
| `tail()` | Display last N rows |
| `info()` | Data types, non-null counts, memory |
| `describe()` | Statistical summary |
| `shape` | Dimensions (rows, columns) |
| `size` | Total elements |
| `ndim` | Number of dimensions |
| `columns` | Column names |
| `index` | Row index |
| `dtypes` | Data types per column |
| `memory_usage()` | Memory consumption |

### 3️⃣ Data Selection & Indexing
| Method | Description |
|--------|-------------|
| `loc[]` | Label-based selection |
| `iloc[]` | Position-based selection |
| `at[]` | Fast scalar by label |
| `iat[]` | Fast scalar by position |
| `[]` | Column selection |
| `query()` | Filter with string expression |

### 4️⃣ Data Analysis
| Method | Description |
|--------|-------------|
| `value_counts()` | Frequency distribution |
| `unique()` | Unique values |
| `nunique()` | Count unique values |
| `sum()` | Sum of values |
| `mean()` | Average |
| `median()` | Median value |
| `min()` / `max()` | Min/Max values |
| `count()` | Non-null count |

### 5️⃣ Data Manipulation
| Method | Description |
|--------|-------------|
| `sort_values()` | Sort by column |
| `sort_index()` | Sort by index |
| `sample()` | Random sampling |
| `copy()` | Create copy |
| `rename()` | Rename columns |

### 6️⃣ Missing Data
| Method | Description |
|--------|-------------|
| `isna()` | Detect missing |
| `notna()` | Detect non-missing |
| `isna().sum()` | Count missing |

### 7️⃣ GroupBy Operations
| Method | Description |
|--------|-------------|
| `groupby()` | Group data |
| `agg()` | Multiple aggregations |

---

## 📁 Project Files

```
project_1_titanic/
├── README.md              # This documentation
├── titanic_analysis.ipynb # Jupyter Notebook (cell-by-cell learning)
├── titanic_analysis.py    # Python script
└── titanic_app.py         # Streamlit UI Application
```

---

## 🚀 How to Run

### Jupyter Notebook
```bash
jupyter notebook titanic_analysis.ipynb
```

### Python Script
```bash
python titanic_analysis.py
```

### Streamlit UI
```bash
streamlit run titanic_app.py
```

---

## 📈 Key Insights (Preview)

- **Survival Rate**: ~38% passengers survived
- **Gender Impact**: Females had higher survival rate (~74%)
- **Class Impact**: 1st class passengers survived more (~63%)
- **Age Factor**: Children had better survival chances

---

## 🎯 Learning Outcomes

After completing this project, you will master:
- ✅ Loading and inspecting data
- ✅ Understanding DataFrame structure
- ✅ Selecting and filtering data
- ✅ Basic statistical analysis
- ✅ GroupBy operations
- ✅ Missing data detection
- ✅ Building interactive dashboards

---

## 👨‍💻 Author

Portfolio Project - Pandas Mastery Series
