# Celebal Technologies - Summer Internship

Personal coursework repository for a **2-month summer internship** at [Celebal Technologies](https://www.celebaltechnologies.com/). Weekly assignments on Python, data science, and machine learning fundamentals are submitted here as Jupyter notebooks.

**Intern:** Avi Mathur  
**Duration:** 2 months (summer)  
**Format:** One notebook per week

---

## Repository layout

Assignments are added to this repo as they are released. Expected pattern:

```
.
├── README.md
├── Customer-data.csv                        # Customer behavior & churn dataset
├── tesla_deliveries_dataset_2015_2025.csv   # Tesla sales & production dataset
├── week1_Avi_Mathur.ipynb                   # Python Fundamentals (complete)
├── week2_Avi_Mathur.ipynb                   # End-to-End ML Pipeline (complete)
├── week3_Avi_Mathur.ipynb                   # Customer Intelligence System (complete)
└── ...
```

| Week | Notebook | Topics | Status |
|------|----------|--------|--------|
| 1 | `week1_Avi_Mathur.ipynb` | Python, NumPy, Pandas, linear algebra, statistics, probability | Done |
| 2 | `week2_Avi_Mathur.ipynb` | End-to-End ML Pipeline (Preprocessing, EDA, Regression, Forecasting) | Done |
| 3 | `week3_Avi_Mathur.ipynb` | Customer Intelligence System (Feature Engineering, Classification, Clustering) | Done |
| 4+ | … | Per internship schedule | Upcoming |

---

## Week 1 — Python Fundamentals

- **Part 1:** Python (control flow, data structures, exceptions, functions)
- **Part 2:** NumPy (arrays, indexing, linear algebra ops)
- **Part 3:** Pandas (DataFrames, `iloc`/`loc`, groupby, missing data)

---

## Week 2 — End-to-End ML Pipeline on Tesla Data

- **Data Preprocessing & Pipelines:** Handled missing values, scaled numerical features, and one-hot encoded categorical features using scikit-learn's `Pipeline` and `ColumnTransformer`.
- **Exploratory Data Analysis (EDA):** Visualized deliveries and production trends by region/model over time, analyzed correlation matrices, and delivery distributions.
- **Regression Modeling & Tuning:** Built and evaluated `LinearRegression`, `Ridge` (L2), and `Lasso` (L1) models to predict `Estimated_Deliveries`. Performed hyperparameter tuning using `GridSearchCV`.
- **Forecasting Insights:** Built a forecasting model leveraging lag-based features and chronological train-test splits to predict future Tesla delivery trends.

---

## Week 3 — Customer Intelligence System

- **Feature Engineering & Preprocessing:** Engineered a composite **Loyalty Score** combining normalized spending score, frequency, and inverse recency. Applied log transformations to right-skewed columns (`Monetary` and `Annual_Income`) to stabilize variance. Scaled features and prepared stratified splits.
- **Supervised Classification:** Trained and cross-validated Logistic Regression, Random Forest, and XGBoost models to predict customer value segments (`Low-Value`, `Mid-Value`, `High-Value`). Logistic Regression achieved the highest classification test accuracy of **98.5%**.
- **Unsupervised Clustering:** Grouped customers using K-Means ($K=2$) and DBSCAN ($\epsilon=1.2$) based on Recency, Frequency, and Monetary (RFM) metrics. Visualized and profiled natural groupings.
- **Priority Customer Retention:** Developed a Retention Priority Score to identify high-risk, high-value active customers, mapping priority tiers to assist targeted marketing campaigns.

---

## Running a notebook

1. Open the repo in VS Code or Jupyter.
2. Select a kernel with the packages above installed.
3. **Kernel → Restart & Run All** on the target notebook.
4. Confirm all `assert` cells pass and plots render with titles and axis labels.

Week 1 should run top-to-bottom without errors after Part 3 creates `df_filled` (used in later sections).
Week 2 requires `tesla_deliveries_dataset_2015_2025.csv` to be present in the root directory.
Week 3 requires `Customer-data.csv` to be present in the root directory.

---

## Submission convention

- Saved my notebooks as `week<number>_Avi_Mathur.ipynb`.

---

## Notes

- This repo is for **internship assignments only**; new weeks will be committed as they are assigned.

---

*Last updated: June 2026 — Week 3 complete.*
