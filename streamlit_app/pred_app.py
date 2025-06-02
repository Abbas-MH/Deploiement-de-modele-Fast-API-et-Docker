import streamlit as st
import pandas as pd
import requests

st.title("Prédiction de Churn via un fichier CSV")

uploaded_file = st.file_uploader("Chargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lire le CSV
    df = pd.read_csv(uploaded_file, sep=';', decimal=',')

    st.write("Aperçu des données chargées :")
    st.dataframe(df.head())

    # URL de l'API
    api_url = "https://deploiement-de-modele-fast-api-et-docker.onrender.com/predict"

    results = []

    with st.spinner("Prédiction en cours..."):
        for index, row in df.iterrows():
            # Convertir chaque ligne en dictionnaire pour l'envoyer à l'API
            data = row.to_dict()

            try:
                response = requests.post(api_url, json=data)

                if response.status_code == 200:
                    prediction = response.json()["prediction"]
                else:
                    prediction = f"Erreur {response.status_code}"

            except Exception as e:
                prediction = f"Erreur: {e}"

            results.append(prediction)

    df["Prediction"] = results

    st.success("Prédictions terminées")
    st.dataframe(df)

    # Option de téléchargement
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Télécharger les résultats", data=csv, file_name="churn_predictions.csv", mime="text/csv")
