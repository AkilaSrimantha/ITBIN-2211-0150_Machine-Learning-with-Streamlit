

# 🍷 Wine Quality Prediction App

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deployed on Streamlit Cloud](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-FF4B4B?logo=streamlit)](https://itbin-2211-0150machine-learning-model-deployment-with-app-mias.streamlit.app/)

---

## 📌 Overview
This project is a **Machine Learning + Streamlit** application that predicts whether a wine is **Good** or **Not Good** based on its chemical properties.  
The model was trained on the [Wine Quality (Red) Dataset]([https://archive.ics.uci.edu/ml/datasets/Wine+Quality](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)) from the UCI Machine Learning Repository.  
It demonstrates the complete ML pipeline: **data preprocessing → model training → evaluation → deployment**.

---

## 📂 Project Structure
wine_quality_project/
├── app.py # Streamlit application
├── model.pkl # Saved trained model
├── requirements.txt # Dependencies
├── data/
│ └── WineQT.csv
├── notebooks/
│ └── model_training.ipynb
└── README.md


---

## 📊 Dataset Information

- **Source:** UCI Machine Learning Repository  
- **Records:** 1,599 red wine samples  
- **Features:** 11 physicochemical attributes:
  - Fixed acidity
  - Volatile acidity
  - Citric acid
  - Residual sugar
  - Chlorides
  - Free sulfur dioxide
  - Total sulfur dioxide
  - Density
  - pH
  - Sulphates
  - Alcohol
  - Water
  - 
- **Target Variable:** Quality score (converted to binary classification: Good ≥ 6, Not Good < 6)

---

## 🛠 Installation & Setup
##1️⃣ Clone the Repository

git clone [https://github.com/<AkilaSrimantha>/wine-quality-prediction.git](https://github.com/AkilaSrimantha/ITBIN-2211-0150_Machine-Learning-with-Streamlit.git)
cd wine-quality-prediction

2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Run the Application Locally
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🚀 Deployment
The app is deployed on Streamlit Cloud and accessible via the following link:https://itbin-2211-0150machine-learning-model-deployment-with-app-mias.streamlit.app/
🔗 Live App

🤖 Model Information
Algorithm Used: Random Forest Classifier

Performance:

Accuracy: ~88%

Evaluation metrics: Accuracy, Precision, Recall, F1-score

Model Saving: Stored as model.pkl using Python’s pickle module.

📸 App Features
Data Exploration: View dataset overview & summary statistics.

Visualizations: Interactive correlation heatmap.

Prediction: Sliders to set wine chemical properties and get instant predictions.




📚 References
Cortez, P., et al. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems, 47(4), 547–553.

UCI Machine Learning Repository – Wine Quality Dataset

Streamlit Documentation

Scikit-learn Documentation
