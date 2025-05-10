
import os
import streamlit as st
import joblib
import pandas as pd

# Charger le modèle entraîné
@st.cache_resource
def load_model():
    model_path = "modele.pkl"  # Utilisez un chemin relatif
    if not os.path.exists(model_path):
        st.error(f"Le fichier {model_path} est introuvable. Assurez-vous qu'il est présent dans le répertoire du projet.")
        return None
    try:
        with open(model_path, "rb") as file:
            model = joblib.load(file)
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {str(e)}")
        return None

# Charger le modèle
model = load_model()

# Vérifiez si le modèle est valide
if model and not hasattr(model, "predict"):
    st.error("Le modèle chargé n'a pas de méthode 'predict'. Vérifiez que vous avez bien enregistré un modèle scikit-learn valide.")
elif not model:
    st.error("Le modèle n'a pas pu être chargé correctement. Veuillez vérifier le fichier.")

# Interface utilisateur
st.title("Déploiement d'un modèle LogisticRegression")

st.subheader("Simulation")

# Champs d'entrée utilisateur
three_g = st.radio("Le téléphone possède-t-il la 3G?", ["Oui", "Non"]) 
touch_screen = st.radio("Le téléphone possède-t-il l'écran tactile?", ["Oui", "Non"]) 
wifi  = st.radio("Le téléphone possède-t-il le Wi-Fi ?", ["Oui", "Non"]) 
dual_sim   = st.radio("Le téléphone prend-t-il en charge la double carte SIM ?", ["Oui", "Non"]) 
blue= st.radio("Le téléphone possède-t-il un Bluetooth?", ["Oui", "Non"]) 
battery_power = st.number_input("Énergie totale qu'une batterie peut stocker en une seule fois en mAh ?", min_value=0, step=1, format="%d")
clock_speed=st.number_input("La vitesse à laquelle le microprocesseur exécute les instructions?", min_value=0.0, step=0.1, format="%.1f")
fc = st.number_input("Les Mégapixels de la caméra frontale?", min_value=0, step=1, format="%d")
int_memory=st.number_input("La Mémoire interne en gigaoctets?", min_value=0, step=1, format="%d")
m_dep = st.number_input("La Profondeur du mobile en cm ?", min_value=0.0, step=0.1, format="%.1f")
mobile_wt=st.number_input("Le Poids du téléphone portable?", min_value=0, step=1, format="%d")
n_cores=st.number_input("Le nombre de cœurs du processeur?", min_value=0, step=1, format="%d")
pc= st.number_input("Les mégapixels de l'appareil photo principal?", min_value=0, step=1, format="%d")
px_height=st.number_input("La résolution en pixels Hauteur?", min_value=0, step=1, format="%d")
px_width=st.number_input("La largeur de résolution en pixels?", min_value=0, step=1, format="%d")
ram=st.number_input("La mémoire à accès aléatoire en mégaoctets?", min_value=0, step=1, format="%d")
sc_h=st.number_input("La hauteur de l'écran du mobile en cm?", min_value=0, step=1, format="%d")
sc_w=st.number_input("La largeur de l'écran du mobile en cm?", min_value=0, step=1, format="%d")
talk_time=st.number_input("La durée la plus longue pendant laquelle une seule charge de batterie durera?", min_value=0, step=1, format="%d")

if st.button("Envoyer"):
    try:
        # Afficher les données saisies par le client
        st.subheader("Données saisies par le client :")
        donne = pd.DataFrame({
            "Le téléphone possède-t-il la 3G?": [three_g],
            "Le téléphone possède-t-il l'écran tactile?": [touch_screen],
            "Le téléphone possède-t-il le Wi-Fi ?": [wifi],
            "Le téléphone prend-t-il en charge la double carte SIM?": [dual_sim],
            "Le téléphone possède-t-il un Bluetooth?": [blue],
            "Quelle est l'Énergie totale qu'une batterie peut stocker en une seule fois en mAh?": [battery_power],
            "Quelle est la vitesse à laquelle le microprocesseur exécute les instructions?": [clock_speed],
            "Quels sont les Mégapixels de la caméra frontale?": [fc],            
            "Quelle est la Mémoire interne en gigaoctets?": [int_memory],
            "Quelle est la Profondeur du mobile en cm?": [m_dep],
            "Quel est le Poids du téléphone portable?": [mobile_wt],
            "Quel est le nombre de cœurs du processeur?": [n_cores],
            "Quels sont les mégapixels de l'appareil photo principal?": [pc],
            "Quelle est la résolution en pixels Hauteur?": [px_height],
            "Quelle est la largeur de résolution en pixels?": [px_width],            
            "Quelle est la mémoire à accès aléatoire en mégaoctets?": [ram],
            "Quelle est la hauteur de l'écran du mobile en cm?": [sc_h],
            "Quelle est la largeur de l'écran du mobile en cm?": [sc_w],
            "Quelle est la durée la plus longue pendant laquelle une seule charge de batterie durera?": [talk_time]
        })
        st.write(donne)

        # Préparer les données utilisateur
        three_g_encoded = True if three_g == "Oui" else False 
        touch_screen_encoded = True if touch_screen == "Oui" else False 
        wifi_encoded = True if wifi == "Oui" else False  
        dual_sim_encoded = True if dual_sim == "Oui" else False  
        blue_encoded = True if blue == "Oui" else False  

        # Création du DataFrame d'entrée
        input_data = pd.DataFrame({
            "three_g": [three_g_encoded],
            "touch_screen": [touch_screen_encoded],
            "wifi": [wifi_encoded],
            "dual_sim": [dual_sim_encoded],
            "blue": [blue_encoded],
            "battery_power": [battery_power],
            "clock_speed": [clock_speed],
            "fc": [fc],            
            "int_memory": [int_memory],
            "m_dep": [m_dep],
            "mobile_wt": [mobile_wt],
            "n_cores": [n_cores],
            "pc": [pc],
            "px_height": [px_height],
            "px_width": [px_width],            
            "ram": [ram],
            "sc_h": [sc_h],
            "sc_w": [sc_w],
            "talk_time": [talk_time]
        })

        # Prédiction avec le modèle
        if model:
            prediction = model.predict(input_data)
            if prediction[0]==0:
                st.success(f"Le téléphone avec un prix faible : {prediction[0]:} ")
            elif prediction[0]==1:
                st.success(f"Le téléphone est dans une fourchette de prix intermédiaire, mais encore abordables: {prediction[0]:} ")
            elif prediction[0]==2:    
                st.success(f" Téléphone avec un prix un peu plus élevé, offrant des spécifications plus avancées que les téléphones précédents, mais restant inférieurs aux modèles haut de gamme.: {prediction[0]:} ")
            else:
                st.success(f"Le téléphone est dans une fourchette de prix élevée.: {prediction[0]:} ")
                
    except Exception as e:
        st.error(f"Une erreur est survenue : {str(e)}")
