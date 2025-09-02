# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger modèle et scaler
kmeans = joblib.load('model/kmeans_model.pkl')
scaler = joblib.load('model/scaler.pkl')

# Mapping cluster -> profil et action
profil_dict = {
    0: "Seniors, revenu moyen, dépense moyenne",
    1: "Jeunes adultes à haut revenu, dépense élevée",
    2: "Jeunes, revenu faible, dépense élevée",
    3: "Jeunes adultes, revenu moyen, dépense moyenne",
    4: "Adultes à revenu élevé, faible dépense",
    5: "Adultes, faible revenu et faible dépense"
}

action_dict = {
    0: "Offres d’épargne, fidélisation",
    1: "Promotions sur produits premium, cross-sell",
    2: "Offres abordables, cartes fidélité, mobile",
    3: "Promotions ciblées, offres régulières",
    4: "Cross-sell assurance/épargne, fidélisation",
    5: "Produits d’épargne simples, sensibilisation à services"
}

app = FastAPI()

class Client(BaseModel):
    Age: float
    AnnualIncome: float
    SpendingScore: float

@app.post("/predict/")
def predict_segment(client: Client):
    data = np.array([[client.Age, client.AnnualIncome, client.SpendingScore]])
    data_scaled = scaler.transform(data)
    cluster = kmeans.predict(data_scaled)[0]
    profil = profil_dict[cluster]
    action = action_dict[cluster]
    return {"Cluster": int(cluster), "Profil_type": profil, "Action_marketing": action}
