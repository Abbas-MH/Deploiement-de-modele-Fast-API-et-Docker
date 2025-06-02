import json
import pandas as pd

# Charger expected_cols
with open('expected_columns.json', 'r') as f:
    expected_cols = json.load(f)

def preprocess_input(df):
    

    # Encodage binaire : 1 = Yes/Female, 0 = No ou autre
    df['gender'] = df['gender'].apply(lambda x: 1 if x == 'Female' else 0)
    binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    for col in binary_cols:
        df[col] = df[col].apply(lambda x: 1 if x == 'Yes' else 0)

    # Colonnes catégorielles à encoder avec get_dummies
    cat_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']
    
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # À ce stade, df contient les colonnes encodées
    df_transformed = df.copy()

    # Ajouter colonnes manquantes (remplies avec 0)
    for col in expected_cols:
        if col not in df_transformed.columns:
            df_transformed[col] = 0

    # Supprimer colonnes inattendues et réordonner
    df_transformed = df_transformed[expected_cols]

    return df_transformed
