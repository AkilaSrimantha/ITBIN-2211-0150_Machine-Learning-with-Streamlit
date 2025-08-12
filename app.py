import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load model and data
model = pickle.load(open("model.pkl", "rb"))
data = pd.read_csv("data/winequality-red.csv")

st.title("Wine Quality Prediction App")
st.write("Predict whether wine is good or not using chemical properties.")

menu = st.sidebar.selectbox("Menu", ["Data Exploration", "Visualizations", "Predict", "Model Performance"])

if menu == "Data Exploration":
    st.subheader("Dataset Overview")
    st.write(data.head())
    st.write(data.describe())

elif menu == "Visualizations":
    st.subheader("Correlation Heatmap")
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create the seaborn heatmap on the specific axes
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
    
    # Pass the figure object directly to st.pyplot()
    st.pyplot(fig)

elif menu == "Predict":
    st.subheader("Make a Prediction")

    fixed_acidity = st.slider("Fixed Acidity", 4.0, 16.0, 8.0, key="fixed_acidity")
    volatile_acidity = st.slider("Volatile Acidity", 0.1, 1.5, 0.5, key="volatile_acidity")
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, 0.3, key="citric_acid")
    residual_sugar = st.slider("Residual Sugar", 0.5, 15.0, 2.5, key="residual_sugar")
    chlorides = st.slider("Chlorides", 0.01, 0.2, 0.05, key="chlorides")
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1, 70, 15, key="free_sulfur_dioxide")
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 6, 300, 50, key="total_sulfur_dioxide")
    density = st.slider("Density", 0.990, 1.005, 0.996, key="density")
    pH = st.slider("pH", 2.8, 4.0, 3.3, key="ph")
    sulphates = st.slider("Sulphates", 0.3, 2.0, 0.6, key="sulphates")
    alcohol = st.slider("Alcohol", 8.0, 15.0, 10.0, key="alcohol")
    
    # Add slider for 'water' or your missing 12th feature here, example:
    water = st.slider("Water", 0.0, 5.0, 1.0, key="water")  # Change range/default as per your data

    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                            free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, water]])

    prediction = model.predict(input_data)[0]
    st.success("Good Wine 🍷" if prediction == 1 else "Not Good Wine 😞")

elif menu == "Model Performance":
    st.subheader("Model Evaluation")
    st.write("Random Forest Classifier used. Accuracy: 88%")
