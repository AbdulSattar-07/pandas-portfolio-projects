# 🛒 Project 2: E-Commerce Data Cleaning Pipeline

## 📋 Project Overview

Online Retail dataset ka professional data cleaning - missing values, duplicates, outliers, aur data quality issues handle karna. Real-world ETL workflow.

---

## 📊 Dataset Information

| Feature | Description |
|---------|-------------|
| **InvoiceNo** | Invoice number (unique per transaction) |
| **StockCode** | Product code |
| **Description** | Product name |
| **Quantity** | Quantity purchased |
| **InvoiceDate** | Date and time of transaction |
| **UnitPrice** | Price per unit |
| **CustomerID** | Customer identifier |
| **Country** | Customer's country |

---

## 🐼 Pandas Topics Covered (20+ Methods)

### 1️⃣ Missing Data Detection
| Method | Description |
|--------|-------------|
| `isna()` | Detect NaN values |
| `isnull()` | Same as isna() |
| `notna()` | Detect non-NaN values |
| `notnull()` | Same as notna() |

### 2️⃣ Missing Data Handling
| Method | Description |
|--------|-------------|
| `fillna()` | Fill missing values |
| `dropna()` | Remove rows/cols with missing |
| `interpolate()` | Interpolate missing values |

### 3️⃣ Duplicate Handling
| Method | Description |
|--------|-------------|
| `duplicated()` | Find duplicate rows |
| `drop_duplicates()` | Remove duplicates |

### 4️⃣ Data Type Conversion
| Method | Description |
|--------|-------------|
| `astype()` | Convert data types |
| `to_datetime()` | Convert to datetime |
| `to_numeric()` | Convert to numeric |

### 5️⃣ Data Replacement & Filtering
| Method | Description |
|--------|-------------|
| `replace()` | Replace values |
| `where()` | Conditional replacement |
| `mask()` | Inverse of where() |
| `clip()` | Limit values to range |
| `query()` | Filter with expression |

### 6️⃣ Data Manipulation
| Method | Description |
|--------|-------------|
| `sort_values()` | Sort by column |
| `sort_index()` | Sort by index |
| `copy()` | Create DataFrame copy |
| `select_dtypes()` | Select columns by dtype |
| `assign()` | Add new columns |

### 7️⃣ String Operations
| Method | Description |
|--------|-------------|
| `str.strip()` | Remove whitespace |
| `str.upper()` | Convert to uppercase |
| `str.lower()` | Convert to lowercase |
| `str.contains()` | Check if contains pattern |

---

## 📁 Project Files

```
project_2_ecommerce/
├── README.md                  # This documentation
├── ecommerce_cleaning.ipynb   # Jupyter Notebook
├── ecommerce_cleaning.py      # Python script
├── ecommerce_app.py           # Streamlit Dashboard
└── requirements.txt           # Dependencies
```

---

## 🚀 How to Run

```bash
# Jupyter Notebook
jupyter notebook ecommerce_cleaning.ipynb

# Python Script
python ecommerce_cleaning.py

# Streamlit Dashboard
streamlit run ecommerce_app.py
```

---

## 🎯 Learning Outcomes

- ✅ Detect and handle missing values
- ✅ Remove duplicate records
- ✅ Convert data types properly
- ✅ Handle outliers and invalid data
- ✅ String cleaning operations
- ✅ Build reusable cleaning pipeline
- ✅ Export cleaned data

---

## 👨‍💻 Author

Portfolio Project - Pandas Mastery Series
