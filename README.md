# API de Prédiction du Churn avec Régression Logistique

## Description

Ce projet consiste à créer une API REST pour prédire le churn (résiliation client) en utilisant un modèle de régression logistique.  
Le modèle a été entraîné puis sauvegardé avec **joblib**.  
L’API **FastAPI** reçoit les données brutes, les prétraite avant de faire la prédiction.  
Le tout est conteneurisé avec **Docker** et déployé sur le cloud.

---

##  📁 Structure du projet


├── main.py # Application FastAPI principale

├── preprocessing.py  # Fonction de preprocessing des données d'entrée

├── logreg_model.joblib # Modèle de régression logistique sauvegardé

├── column_order.joblib # Ordre attendu des colonnes après preprocessing

├── expected_columns.json # Colonnes attendues après encodage

├── requirements.txt # Dépendances Python

├── Dockerfile # Fichier pour construire 
l'image Docker

├── .dockerignore # Fichier pour exclure des fichiers dans l'image Docker

└── README.md # Ce fichier


---

## Étapes de réalisation

### 1. Entraînement et sauvegarde du modèle

- Modèle de régression logistique entraîné sur données préalablement préparées.
- Sauvegarde du modèle avec **joblib** dans `logreg_model.joblib`.
- Sauvegarde de l’ordre des colonnes dans `column_order.joblib` pour assurer une cohérence des données en entrée.

### 2. Prétraitement des données (`preprocessing.py`)

- Encodage des variables binaires (Yes/No, Female/Male) en 0/1.
- Encodage des variables catégorielles avec `pd.get_dummies` (one-hot encoding).
- Gestion des colonnes manquantes et réordonnancement selon la structure attendue (`expected_columns.json`).

### 3. Création de l’API avec FastAPI (`main.py`)

- Définition du schéma d’entrée avec **Pydantic** pour valider les données reçues.
- Conversion des données reçues en DataFrame **Pandas**.
- Application du preprocessing.
- Réalignement des colonnes selon l’ordre attendu.
- Prédiction du churn avec le modèle chargé.
- Retour de la prédiction sous forme simple (**Churn** / **No Churn**).

### 4. Conteneurisation avec Docker

- Utilisation d’une image Python légère (`python:3.11-slim`).
- Installation des dépendances via `requirements.txt`.
- Copie des fichiers sources dans le conteneur.
- Lancement du serveur **Uvicorn** pour exposer l’API sur le port 80.

### 5. Déploiement sur le cloud

- Push de l’image Docker vers un service de cloud (**Render**).
- L’API est accessible publiquement via l’URL :  
  [https://deploiement-de-modele-fast-api-et-docker.onrender.com](https://deploiement-de-modele-fast-api-et-docker.onrender.com)

---

## Utilisation

### Exemple de requête POST `/predict`


{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 1,
  "PhoneService": "No",
  "MultipleLines": "No phone service",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 29.85,
  "TotalCharges": 29.85
}


### Réponse

{
"prediction": "Churn"
}


---

## Technologies utilisées

- Python 3.11
- FastAPI
- Pandas
- Scikit-learn (pour le modèle)
- Joblib (sauvegarde/chargement modèle)
- Docker
- Uvicorn
- Render (hébergement cloud)

---

## Points forts

- Pipeline complet du modèle ML au déploiement en production.
- Architecture modulaire avec séparation du preprocessing et de l’API.
- Conteneurisation pour portabilité et scalabilité.
- Documentation claire du format d’entrée et du workflow.

---

## Voir l’API en action

L’API est accessible ici :  
[https://deploiement-de-modele-fast-api-et-docker.onrender.com](https://deploiement-de-modele-fast-api-et-docker.onrender.com)
