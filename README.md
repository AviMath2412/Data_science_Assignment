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
├── week4_Avi_Mathur.ipynb                   # CIFAR-10 Image Classification (complete)
├── week5_Avi_Mathur.ipynb                   # Deep Learning Text Generation (complete)
└── ...
```

| Week | Notebook | Topics | Status |
|------|----------|--------|--------|
| 1 | `week1_Avi_Mathur.ipynb` | Python, NumPy, Pandas, linear algebra, statistics, probability | Done |
| 2 | `week2_Avi_Mathur.ipynb` | End-to-End ML Pipeline (Preprocessing, EDA, Regression, Forecasting) | Done |
| 3 | `week3_Avi_Mathur.ipynb` | Customer Intelligence System (Feature Engineering, Classification, Clustering) | Done |
| 4 | `week4_Avi_Mathur.ipynb` | CIFAR-10 Image Classification (ANN vs CNN, Data Augmentation) | Done |
| 5 | `week5_Avi_Mathur.ipynb` | Deep Learning Text Generation (RNN, LSTM, GRU) | Done |
| 6+ | … | Per internship schedule | Upcoming |

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

## Week 4 — CIFAR-10 Image Classification (ANN vs CNN)

- **Problem Definition:** Built image classification models on the **CIFAR-10 dataset** containing 60,000 color images (32×32×3 pixels) across 10 classes (Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck) to study deep learning fundamentals.
- **Artificial Neural Networks (ANN):** Implemented an ANN model treating images as flat vectors. Demonstrated why ANNs fail to preserve spatial structures, resulting in a baseline test accuracy of **42.4%**.
- **Convolutional Neural Networks (CNN):** Designed a CNN with convolutional layers, batch normalization, max pooling, dropout, and early stopping. Demonstrated the superiority of CNNs in extracting spatial features, achieving a test accuracy of **70.1%**.
- **Training Strategy Upgrades:** Implemented and evaluated **Data Augmentation** (horizontal flips, rotation, and zoom) as a modernization strategy to improve generalization and mitigate overfitting.

---

## Week 5 — Deep Learning Text Generation (RNN, LSTM, GRU)

- **Problem Definition:** Designed and implemented sequential deep learning models capable of learning the structure, grammar, and contextual dependencies of a text corpus to generate coherent next-word predictions and text sequences.
- **Model Architectures & Optimization:** Compared three sequential network architectures:
  - **Vanilla RNN:** Baseline recurrent neural network. Upgraded hidden layers from 64 to 128 units and embedding dimensions from 32 to 64. Trained for 200 epochs, reaching a final loss of **0.0115**, but mathematically prone to vanishing gradients on longer sequences.
  - **LSTM:** Utilized gated memory cell architecture (input, forget, and output gates) to resolve vanishing gradient issues, achieving a final loss of **0.1639**.
  - **GRU:** Used a simplified gated structure (reset and update gates) to achieve a comparable final loss of **0.0178** with faster training times and lower parameter count.
- **Text Generation:** Tokenized and converted text into integer tokens and created n-gram sequences for next-word prediction. Developed a text generator producing coherent 10-word sequences from a prompt (e.g., generating *"deep learning uses multiple layers to extract features from raw data"*).

---

## Running a notebook

1. Open the repo in VS Code or Jupyter.
2. Select a kernel with the packages above installed.
3. **Kernel → Restart & Run All** on the target notebook.
4. Confirm all `assert` cells pass and plots render with titles and axis labels.

Week 1 should run top-to-bottom without errors after Part 3 creates `df_filled` (used in later sections).
Week 2 requires `tesla_deliveries_dataset_2015_2025.csv` to be present in the root directory.
Week 3 requires `Customer-data.csv` to be present in the root directory.
Week 4 automatically downloads the CIFAR-10 dataset via Keras on the first execution (requires internet connection).
Week 5 runs self-contained with a built-in custom text corpus on deep learning concepts.

---

## Submission convention

- Saved my notebooks as `week<number>_Avi_Mathur.ipynb`.

---

## Notes

- This repo is for **internship assignments only**; new weeks will be committed as they are assigned.

---

*Last updated: June 2026 — Week 5 complete.*
