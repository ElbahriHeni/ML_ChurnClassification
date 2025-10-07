import joblib
import streamlit as st
import numpy as np

rf = joblib.load("RandomForestPickleFile")

st.title("Customer Churn Prediction")
st.write("This app predicts if a customer is likely to **exit or stay**")
st.sidebar.header("Enter customer  details")
age = st.sidebar.number_input("Age",min_value=18, max_value=100,value=35)
products = st.sidebar.number_input("Product",min_value=1, max_value=4,value=1)
balance = st.sidebar.number_input("Balance",min_value=0, max_value=250898,value=35)
EstimatedSalary = st.sidebar.number_input("EstimatedSalary",min_value=10, max_value=200000,value=35)
CreditScore = st.sidebar.number_input("CreditScore",min_value=10, max_value=1000,value=35)  
if st.sidebar.button("Predict Churn") :
    features = [[age,balance, products,EstimatedSalary,CreditScore]]
    predict = rf.predict(features)[0]
    if predict == 1:
        st.error("The customer is likely to churn")
    else:
        st.success("The customer is likely to stay")

