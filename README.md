# 📌 Thanks to Bahare Esmaili, Dr. Saeidi, and Dr. Ehsan for providing the dataset...
# Predicting Acute Myeloid Leukemia (AML) Status From HLA Genotypes

This repository contains a full machine learning pipeline to evaluate whether Human Leukocyte Antigen (HLA) genotypes and demographic variables can be used to predict Acute Myeloid Leukemia (AML) status.
Despite extensive modeling, dimensionality reduction, and validation procedures, the findings indicate that **HLA genotypes alone do not provide a sufficiently strong signal for reliable AML classification** within the available dataset.

## 🔬 Project Overview
The goal of this project is to investigate potential immunogenetic patterns associated with AML using classical and modern machine-learning techniques.

We explore:
- Preprocessing and harmonization of multi-locus HLA data
- Encoding strategies for discrete high-dimensional alleles
- Construction of complete and reduced datasets
- Model development across several ML families
- Statistical evaluation, feature importance, and interpretability
- Biological and methodological limitations

This repository includes both code and a full **scientific report (PDF)** summarizing methodology and findings.

## 📁 Repository Contents
- `notebooks/` – Preprocessing, modeling, and analysis notebooks
- `data/` – Data ingestion templates
- `models/` – Trained model objects and evaluation metrics
- `figures/` – Plots and SHAP visualizations
- `AML_HLA_Report.pdf` – Full scientific report
- `README.md` – Project documentation (this file)

## 🧬 Methods Summary

### Dataset Preparation
- 294 individuals with multi-locus HLA genotypes  
- Demographic variables: age, sex  
- Disease variable recoded into a binary AML label  
- Two datasets created:
  - Complete case dataset
  - Reduced-feature dataset  

### Encoding
- One-hot encoding of HLA alleles
- Numerical scaling of demographic variables
- Stratified validation splits

### Models Evaluated
- Logistic Regression (L1/L2)
- Naive Bayes (Gaussian, Bernoulli)
- Random Forest
- Gradient Boosting & LightGBM
- SVM
- k-Nearest Neighbors

### Evaluation Metrics
- Accuracy  
- Precision / Recall / F1  
- ROC-AUC  
- Confusion matrices  
- SHAP feature importance  

## 📊 Results Summary
Across all settings, models produced **moderate accuracy but extremely poor recall for the healthy class**, effectively predicting AML for nearly all subjects.

This suggests:
- Severe class imbalance  
- Sparse allele space  
- Sample size too small for HLA-level inference  
- Limited biological signal from HLA alone  

## 📌 Conclusion
AML status **cannot be reliably predicted** from HLA genotypes alone with the available dataset. Future research should incorporate larger cohorts and multimodal biomedical features.

## 🙏 Acknowledgments
We sincerely thank:

**Bahare Esmailie** and **Dr. Saeidi** — for providing the dataset.  
**Dr. Saeed Reza Kherad Pisheh** — for supervision and scientific guidance.  
**Pouya Mirzaeizadeh** and **Shadi Sefidgar** — for collaboration and contributions.  

## 📄 Citation
```
Mirzaeizadeh, P., Sefidgar, S., Esmailie, B., Saeidi, & Kherad Pisheh, S.R. (2025).
Predicting AML Status from HLA Genotypes Using Machine Learning.
```
