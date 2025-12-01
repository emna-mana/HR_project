# Service RH - Évaluation des Candidats

Application Django pour évaluer la probabilité qu'un candidat soit performant selon ses caractéristiques et son expérience, en utilisant un modèle de régression logistique.

## Fonctionnalités

- ✅ Ajout de nouveaux candidats avec leurs informations complètes
- ✅ Prédiction automatique de la probabilité de placement
- ✅ Affichage de la liste des candidats avec leurs prédictions
- ✅ Détails complets pour chaque candidat
- ✅ Interface moderne et intuitive

## Installation

1. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

2. **Créer les migrations :**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Créer un superutilisateur (optionnel) :**
```bash
python manage.py createsuperuser
```

4. **Lancer le serveur de développement :**
```bash
python manage.py runserver
```

5. **Accéder à l'application :**
   - Interface principale : http://127.0.0.1:8000/
   - Administration Django : http://127.0.0.1:8000/admin/

## Structure du Projet

```
projet/
├── manage.py
├── requirements.txt
├── README.md
├── rh/                          # Application principale
│   ├── models.py               # Modèle Candidat
│   ├── views.py                # Vues de l'application
│   ├── urls.py                 # URLs de l'application
│   ├── admin.py                # Configuration admin
│   ├── ml_model.py             # Module ML pour les prédictions
│   └── templates/              # Templates HTML
│       └── rh/
│           ├── base.html
│           ├── index.html
│           ├── ajouter_candidat.html
│           ├── liste_candidats.html
│           └── detail_candidat.html
├── rh_service/                  # Configuration du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── projet/                      # Dossier contenant les modèles ML
    ├── logistic_regression_model.pkl
    └── scaler.pkl
```

## Modèle de Machine Learning

L'application utilise un modèle de régression logistique pré-entraîné (`logistic_regression_model.pkl`) et un scaler (`scaler.pkl`) pour normaliser les données.

### Caractéristiques utilisées pour la prédiction :

1. **Informations personnelles :**
   - Genre
   - Expérience professionnelle

2. **Résultats académiques :**
   - Pourcentage d'éducation secondaire
   - Pourcentage d'éducation supérieure secondaire
   - Pourcentage de diplôme
   - Pourcentage de test d'entrée
   - Pourcentage MBA

3. **Types et spécialisations :**
   - Type de conseil d'éducation (Central/Others)
   - Spécialisation secondaire (Commerce/Science/Arts)
   - Type de diplôme (Sci&Tech/Comm&Mgmt/Others)
   - Spécialisation MBA (Mkt&HR/Mkt&Fin)

## Utilisation

1. **Ajouter un candidat :**
   - Cliquez sur "Ajouter un Candidat"
   - Remplissez tous les champs du formulaire
   - Cliquez sur "Évaluer le Candidat"
   - La prédiction est automatiquement calculée et enregistrée

2. **Consulter les candidats :**
   - Accédez à "Liste des Candidats" pour voir tous les candidats
   - Cliquez sur "Voir Détails" pour plus d'informations

3. **Re-faire une prédiction :**
   - Sur la page de détails d'un candidat, cliquez sur "Re-faire la Prédiction"

## Notes

- Les fichiers `logistic_regression_model.pkl` et `scaler.pkl` doivent être présents dans le dossier `projet/`
- Le modèle a été entraîné avec des données historiques et peut nécessiter un réentraînement périodique
- Les prédictions sont basées sur des données statistiques et ne garantissent pas le résultat réel

## Technologies Utilisées

- Django 5.1.6
- scikit-learn
- NumPy
- Pandas
- HTML/CSS (interface moderne)

## Auteur

Service RH - Évaluation des Candidats

