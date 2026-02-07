# 🍷 Wine Quality Prediction using Machine Learning

This project predicts the **quality of wine** based on its physicochemical properties such as **alcohol, chlorides, volatile acidity, fixed acidity**, and other chemical attributes.  
The goal is to understand how these features influence wine quality and build a regression model to make accurate predictions.

---

## 📌 Project Overview

- Predicts wine quality using **machine learning regression**
- Compares multiple models to evaluate performance
- Visualizes **predicted vs actual values** using scatter plots
- Saves the trained model for reuse and inference

Built using **Python, pandas, NumPy, scikit-learn, and Matplotlib**.

---

## 🧪 Features Used

The model uses the following chemical properties of wine:

- Fixed Acidity  
- Volatile Acidity  
- Citric Acid  
- Residual Sugar  
- Chlorides  
- Free Sulfur Dioxide  
- Total Sulfur Dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  

---

## 📂 File Structure
├── Main.ipynb

├── model.py

├── WineQuality.csv

└── predictions.csv


### 📄 File Descriptions

- **Main.ipynb**  
  Contains data exploration, model comparison, evaluation metrics, and a scatter plot comparing predicted vs actual wine quality.

- **model.py**  
  Handles data loading, train-test splitting, model training, saving/loading using joblib, and inference.

- **WineQuality.csv**  
  Full dataset containing physicochemical features and wine quality labels.

- **predictions.csv**  
  CSV file containing predicted wine quality values for the test dataset.
  
---

## 📊 Dataset Source

The dataset is sourced from Kaggle.

🔗 **Kaggle Dataset Link:**  
👉 https://www.kaggle.com/datasets/boiniabhiram/wine-quality-dataset

---

## 🚀 How to Run the Project

### 1️⃣ Clone this repo
git clone https://github.com/MayankRao2006/wine-quality-prediction.git
