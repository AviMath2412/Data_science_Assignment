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
├── tesla_deliveries_dataset_2015_2025.csv   # Tesla sales & production dataset
├── week1_Avi_Mathur.ipynb                   # Python Fundamentals (complete)
├── week2_Avi_Mathur.ipynb                   # End-to-End ML Pipeline (complete)
├── week3_Avi_Mathur.ipynb                   # upcoming
└── ...
```

| Week | Notebook | Topics | Status |
|------|----------|--------|--------|
| 1 | `week1_Avi_Mathur.ipynb` | Python, NumPy, Pandas, linear algebra, statistics, probability | Done |
| 2 | `week2_Avi_Mathur.ipynb` | End-to-End ML Pipeline (Preprocessing, EDA, Regression, Forecasting) | Done |
| 3+ | … | Per internship schedule | Upcoming |

---

## Week 1 — Python Fundamentals

- **Part 1:** Python (control flow, data structures, exceptions, functions)
- **Part 2:** NumPy (arrays, indexing, linear algebra ops)
- **Part 3:** Pandas (DataFrames, `iloc`/`loc`, groupby, missing data)

---

## Week 2 — End-to-End ML Pipeline on Tesla Data

- **Data Preprocessing & Pipelines:** Handled missing values, scaled numerical features, and one-hot encoded categorical features using scikit-learn's `Pipeline` and `ColumnTransformer`.
- **Exploratory Data Analysis (EDA):** Visualized deliveries and production trends by region/model over time, analyzed correlation matrices, and delivery distributions.
- **Regression Modeling & Tuning:** Built and evaluated `LinearRegression` and `RandomForestRegressor` models to predict `Estimated_Deliveries`. Performed hyperparameter tuning using `GridSearchCV`.
- **Forecasting Insights:** Built a forecasting model leveraging lag-based features and chronological train-test splits to predict future Tesla delivery trends.

---

## Running a notebook

1. Open the repo in VS Code / Cursor or Jupyter.
2. Select a kernel with the packages above installed.
3. **Kernel → Restart & Run All** on the target notebook.
4. Confirm all `assert` cells pass and plots render with titles and axis labels.

Week 1 should run top-to-bottom without errors after Part 3 creates `df_filled` (used in later sections).
Week 2 requires `tesla_deliveries_dataset_2015_2025.csv` to be present in the root directory.

---

## Submission convention

- Save notebooks as `week<number>_Avi_Mathur.ipynb`.
- Keep assignment instructions and cell structure unchanged unless told otherwise.
- Fill all `# YOUR CODE HERE` cells and reflection markdown in your own words before pushing.

---

## Notes

- This repo is for **internship assignments only**; new weeks will be committed as they are assigned.
- Do not commit secrets, API keys, or private datasets.

---

*Last updated: May 2026 — Week 2 complete.*
