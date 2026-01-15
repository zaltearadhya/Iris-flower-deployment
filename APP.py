import streamlit as st
import pickle
import numpy as np

#Load model
with open("model.pkl") as f:
    model=pickle.load(f)

# Streamlit UI
st.title("Iris flower Classifier")
st.write("Enter the features below: ")

s1=st.number_input("Sepal length: ",min_value=4.3,max_value=7.9)
sw=st.number_input("Sepal width: ",min_value=2,max_value=4.4)
pl=st.number_input("petal length: ",min_value=1,max_value=6.9)
pw=st.number_input("petal width: ",min_value=0.1,max_value=2.5)

# Button Predict
if st.button("Predict"):
    pred=model.predict([[sl,sw,pl,pw]])
    classes=["Setosa","Versicolor","Virginica"]
    st.write(f"Prediction: ",{classes[prediction[0]]})
    


