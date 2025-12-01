from django.contrib import admin
from .models import Candidat

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('genre', 'secondary_education_p', 'degree_p', 'mba_p', 'work_experience')
    list_filter = ('genre', 'work_experience', 'degree_type', 'specialisation')
    fieldsets = (
        ('Informations de base', {
            'fields': ('genre', 'work_experience')
        }),
        ('Éducation Secondaire', {
            'fields': ('secondary_education_p', 'education_board_type')
        }),
        ('Éducation Supérieure Secondaire', {
            'fields': ('higher_secondary_p', 'h_education_board_type', 'higher_secondary_specialization')
        }),
        ('Diplôme', {
            'fields': ('degree_p', 'degree_type')
        }),
        ('Tests et MBA', {
            'fields': ('etest_p', 'specialisation', 'mba_p')
        }),
    )
