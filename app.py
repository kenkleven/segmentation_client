# app_streamlit.py
import streamlit as st
import requests

st.title("Segmentation Client - Mall")

age = st.number_input("Age", 18, 70, 30)
income = st.number_input("Annual Income (k$)", 15, 150, 50)
score = st.number_input("Spending Score (1-100)", 1, 100, 50)

if st.button("Prédire le segment"):
    response = requests.post(
        "http://127.0.0.1:8000/predict/",
        json={"Age": age, "AnnualIncome": income, "SpendingScore": score}
    )
    result = response.json()
    st.success(f"Cluster : {result['Cluster']}")
    st.info(f"Profil type : {result['Profil_type']}")
    st.info(f"Action marketing : {result['Action_marketing']}")
