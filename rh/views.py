from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Candidat
from .ml_model import predict_placement

def index(request):
    """Page d'accueil avec navigation"""
    return render(request, 'rh/index.html')

def evaluer_candidat(request):
    """Vue pour évaluer un candidat - sauvegarde automatiquement après évaluation"""
    probabilite = None
    prediction = None
    candidat_sauvegarde = None
    form_data = {}
    
    if request.method == 'POST':
        try:
            # Récupérer les données du formulaire
            form_data = {
                'genre': request.POST.get('genre'),
                'secondary_education_p': request.POST.get('secondary_education_p'),
                'education_board_type': request.POST.get('education_board_type'),
                'higher_secondary_p': request.POST.get('higher_secondary_p'),
                'h_education_board_type': request.POST.get('h_education_board_type'),
                'higher_secondary_specialization': request.POST.get('higher_secondary_specialization'),
                'degree_p': request.POST.get('degree_p'),
                'degree_type': request.POST.get('degree_type'),
                'work_experience': request.POST.get('work_experience'),
                'etest_p': request.POST.get('etest_p'),
                'specialisation': request.POST.get('specialisation'),
                'mba_p': request.POST.get('mba_p'),
            }
            
            # Créer le candidat en base de données
            candidat = Candidat(
                genre=form_data['genre'],
                secondary_education_p=float(form_data['secondary_education_p']),
                education_board_type=form_data['education_board_type'],
                higher_secondary_p=float(form_data['higher_secondary_p']),
                h_education_board_type=form_data['h_education_board_type'],
                higher_secondary_specialization=form_data['higher_secondary_specialization'],
                degree_p=float(form_data['degree_p']),
                degree_type=form_data['degree_type'],
                work_experience=form_data['work_experience'],
                etest_p=float(form_data['etest_p']),
                specialisation=form_data['specialisation'],
                mba_p=float(form_data['mba_p']),
            )
            
            # Faire la prédiction
            probabilite, prediction = predict_placement(candidat)
            candidat.probabilite_performance = probabilite
            candidat.prediction_performance = prediction
            
            # Sauvegarder le candidat
            candidat.save()
            candidat_sauvegarde = candidat
            
            messages.success(request, f'Candidat évalué et sauvegardé avec succès! Probabilité de performance: {probabilite:.2f}%')
            
        except Exception as e:
            messages.error(request, f'Erreur lors de l\'évaluation: {str(e)}')
    
    return render(request, 'rh/evaluer_candidat.html', {
        'probabilite': probabilite,
        'prediction': prediction,
        'candidat': candidat_sauvegarde,
        'form_data': form_data
    })

def liste_candidats(request):
    """Vue pour afficher la liste des candidats triés par probabilité"""
    candidats = Candidat.objects.all()
    return render(request, 'rh/liste_candidats.html', {'candidats': candidats})

def detail_candidat(request, candidat_id):
    """Vue pour afficher les détails d'un candidat"""
    candidat = get_object_or_404(Candidat, id=candidat_id)
    return render(request, 'rh/detail_candidat.html', {'candidat': candidat})
