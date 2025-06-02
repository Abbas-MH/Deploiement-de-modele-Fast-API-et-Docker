from joblib import load
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing import preprocess_input  # Import de ta fonction de preprocessing
import pandas as pd

# Charger le modèle
logreg_model = load("logreg_model.joblib")
column_order = load("column_order.joblib")

# Créer l'app FastAPI
app = FastAPI()

# Définir le schéma des données attendues
class InputData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# Route d'accueil
@app.get("/")
def root():
    return {"message": "API pour prédiction du churn avec modèle de régression logistique"}

# Route de prédiction
@app.post("/predict")
def predict(data: InputData):
    # Convertir les données reçues en DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Appliquer le prétraitement
    processed_df = preprocess_input(input_df)
    processed_df = processed_df.reindex(columns=column_order, fill_value=0)
    

    # Vérifier si les colonnes sont bien présentes
    prediction = logreg_model.predict(processed_df)

    # Interprétation
    prediction_label = "Churn" if prediction[0] == 1 else "No Churn"

    return {"prediction": prediction_label}


