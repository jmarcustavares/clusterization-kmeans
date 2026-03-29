# 🏫 Educational Clustering: Strategic Action Plans via K-Means

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Enabled-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-green.svg)

## 📌 Overview
This project provides a scalable data science solution for a large educational group managing over 1,000 schools. The goal was to move beyond generic dashboards and create actionable, data-driven strategies by grouping schools with similar challenges and strengths.

Using data from the Brazilian **Censo Escolar** and **ENEM** (National High School Exam), this script applies a **K-Means clustering algorithm** to segment schools based on academic performance, physical infrastructure, size, and average tuition.

## 🎯 The Business Challenge
* **Volume & Granularity:** The educational group had over 1,000 schools and dozens of micro-variables from the Censo Escolar.
* **Lack of Actionability:** It is operationally impossible for a management team to design 1,000 individual action plans. They needed a way to consolidate this data into strategic buckets to guide investments, pedagogical interventions, and infrastructure upgrades.

## 💡 The Solution
Instead of analyzing each school individually, we designed a pipeline that:
1. **Aggregates and Models Data:** Curated specific variables to create proprietary indices (e.g., Physical Infrastructure Index - IEF). *(Initial modeling done via SQL)*.
2. **Clusters the Data:** Applied **K-Means (k=5)** to find natural groupings among the schools.
3. **Empowers Decision Making:** Outputs an easily digestible Excel report where each cluster has a defined profile, allowing the board to create 5 macro-strategies instead of 1,000 micro-plans.

## 🛠️ Technical Stack & Pipeline Architecture
* **Language:** Python
* **Libraries:** `pandas`, `numpy`, `scikit-learn`
* **Machine Learning Pipeline:**
  * Uses `ColumnTransformer` for robust preprocessing.
  * Applies `OneHotEncoder` for the categorical variable (`porte` / school size).
  * Passes through already normalized continuous variables (`desempenho`, `IEF`, `media_mensalidade`).
  * Integrates K-Means directly into a `sklearn.pipeline.Pipeline` to prevent data leakage and ensure reproducibility.

## 🚀 How to Run

### 1. Prerequisites
Ensure you have the required libraries installed:
```bash
pip install pandas numpy scikit-learn openpyxl
