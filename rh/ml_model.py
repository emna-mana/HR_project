"""
Module pour charger et utiliser le modèle de régression logistique
"""
import os
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Chemins vers les fichiers du modèle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'projet', 'logistic_regression_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'projet', 'scaler.pkl')

# Variables globales pour stocker le modèle et le scaler
_model = None
_scaler = None

def load_model():
    """Charge le modèle et le scaler depuis les fichiers pickle"""
    global _model, _scaler
    
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    
    return _model, _scaler

def preprocess_data(candidat):
    """
    Prépare les données du candidat pour la prédiction
    Le preprocessing doit correspondre exactement à celui du notebook
    
    Ordre final après toutes les transformations (17 colonnes):
    1. OneHot pour degree_type (3 colonnes: Comm&Mgmt, Others, Sci&Tech)
    2. OneHot pour higher_secondary_specialization (3 colonnes: Arts, Commerce, Science)
    3. Serial_Number
    4. gender (encodé)
    5. SecondaryEducation_p
    6. education_board_type (encodé)
    7. higher_secondary_p
    8. H_education_board_type (encodé)
    9. degree_p
    10. workExperience (encodé)
    11. etest_p
    12. specialisation (encodé)
    13. mba_p
    """
    model, scaler = load_model()
    
    # Étape 1: Encoder les variables catégorielles avec LabelEncoder
    label = LabelEncoder()
    
    # Encoder gender (F=0, M=1)
    label.fit(['F', 'M'])
    gender_encoded = label.transform([candidat.genre])[0]
    
    # Encoder education_board_type
    label.fit(['Central', 'Others'])
    edu_board_encoded = label.transform([candidat.education_board_type])[0]
    
    # Encoder H_education_board_type
    label.fit(['Central', 'Others'])
    h_edu_board_encoded = label.transform([candidat.h_education_board_type])[0]
    
    # Encoder workExperience
    label.fit(['No', 'Yes'])
    work_exp_encoded = label.transform([candidat.work_experience])[0]
    
    # Encoder specialisation
    label.fit(['Mkt&Fin', 'Mkt&HR'])
    spec_encoded = label.transform([candidat.specialisation])[0]
    
    # Étape 2: OneHotEncoder pour degree_type
    # Ordre selon sklearn OneHotEncoder: Comm&Mgmt=0, Others=1, Sci&Tech=2
    # Après transformation: [Comm&Mgmt, Others, Sci&Tech] = [1,0,0], [0,1,0], [0,0,1]
    degree_type_map = {
        'Comm&Mgmt': [1.0, 0.0, 0.0],
        'Others': [0.0, 1.0, 0.0],
        'Sci&Tech': [0.0, 0.0, 1.0]
    }
    degree_type_onehot = degree_type_map.get(candidat.degree_type, [0.0, 0.0, 1.0])
    
    # Étape 3: OneHotEncoder pour higher_secondary_specialization
    # Ordre selon sklearn OneHotEncoder: Arts=0, Commerce=1, Science=2
    # Après transformation: [Arts, Commerce, Science] = [1,0,0], [0,1,0], [0,0,1]
    specialization_map = {
        'Arts': [1.0, 0.0, 0.0],
        'Commerce': [0.0, 1.0, 0.0],
        'Science': [0.0, 0.0, 1.0]
    }
    specialization_onehot = specialization_map.get(candidat.higher_secondary_specialization, [0.0, 0.0, 1.0])
    
    # Construire le tableau final dans l'ordre exact après tous les encodages
    # D'après le test, l'ordre final est:
    # [specialization_onehot (3), degree_type_onehot (3), Serial_Number, gender, 
    #  SecondaryEducation_p, education_board_type, higher_secondary_p, 
    #  H_education_board_type, degree_p, workExperience, etest_p, specialisation, mba_p]
    
    X = np.array([[
        *specialization_onehot,  # 3 colonnes onehot pour higher_secondary_specialization (vient en premier!)
        *degree_type_onehot,  # 3 colonnes onehot pour degree_type
        0,  # Serial_Number
        gender_encoded,
        candidat.secondary_education_p,
        edu_board_encoded,
        candidat.higher_secondary_p,
        h_edu_board_encoded,
        candidat.degree_p,
        work_exp_encoded,
        candidat.etest_p,
        spec_encoded,
        candidat.mba_p
    ]], dtype=float)
    
    # Standardiser les données
    X_scaled = scaler.transform(X)
    
    return X_scaled

def predict_placement(candidat):
    """
    Prédit la probabilité qu'un candidat soit performant après 6 mois
    Retourne: (probabilité, prédiction)
    - probabilité: probabilité de performance après 6 mois (0-100%)
    - prediction: True si performant, False sinon
    """
    model, scaler = load_model()
    
    # Préparer les données
    X = preprocess_data(candidat)
    
    # Faire la prédiction
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]  # Probabilité d'être performant après 6 mois
    
    return probability * 100, bool(prediction)
