import streamlit as st
import pickle
import numpy as np
import sklearn

# Load saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Iris Flower Classifier")
st.write("Enter the features below:")

# Input fields
sepal_length = st.number_input("Sepal Length", min_value=4.0, max_value=8.0)
sepal_width = st.number_input("Sepal Width", min_value=2.0, max_value=5.0)
petal_length = st.number_input("Petal Length", min_value=1.0, max_value=7.0)
petal_width = st.number_input("Petal Width", min_value=0.1, max_value=3.0)

# Predict button
if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    classes = ["Setosa", "Versicolor", "Virginica"]
    st.write(f"Prediction: {classes[prediction[0]]}")
