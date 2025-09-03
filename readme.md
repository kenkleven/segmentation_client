# Segmentation Client 

Ce projet illustre la **segmentation de clients** pour un centre commercial.  
Nous utilisons **KMeans** pour regrouper les clients en fonction de leur âge, revenu et score de dépense, puis nous déployons le modèle avec une API et une interface web streamlit.

---

## Fonctionnalités
- **Clustering KMeans** avec la méthode du coude et le score silhouette pour déterminer `k`
- **Analyse des clusters** avec profils types et actions marketing associées
- **API FastAPI** pour prédire le segment d’un nouveau client
- **Interface Streamlit** pour tester la segmentation en temps réel
- **Containerisation Docker** pour un déploiement facile

---

## Installation

### 1. Cloner le repo
```bash
git https://github.com/kenkleven/segmentation_client.git
cd segmentation_client
```

### 2. Créer un environnement virtuel et installer les dépendances
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Utilisation
```bash
- Lancer l’API
uvicorn api:app --reload
API disponible sur http://127.0.0.1:8000/docs

- Lancer l’application Streamlit
streamlit run app.py

- Déploiement avec Docker
docker build -t segmentation-client .
docker run -p 8501:8501 segmentation-client
```

---
