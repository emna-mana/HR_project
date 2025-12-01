from django.urls import path
from . import views

app_name = 'rh'

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluer/', views.evaluer_candidat, name='evaluer_candidat'),
    path('liste/', views.liste_candidats, name='liste_candidats'),
    path('candidat/<int:candidat_id>/', views.detail_candidat, name='detail_candidat'),
]
