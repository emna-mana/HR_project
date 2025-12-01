from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Candidat(models.Model):
    """Modèle simplifié pour l'évaluation - uniquement les attributs du dataset"""
    
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    
    EDUCATION_BOARD_CHOICES = [
        ('Central', 'Central'),
        ('Others', 'Autres'),
    ]
    
    SPECIALISATION_CHOICES = [
        ('Commerce', 'Commerce'),
        ('Science', 'Science'),
        ('Arts', 'Arts'),
    ]
    
    DEGREE_TYPE_CHOICES = [
        ('Sci&Tech', 'Sciences & Technologie'),
        ('Comm&Mgmt', 'Commerce & Management'),
        ('Others', 'Autres'),
    ]
    
    WORK_EXPERIENCE_CHOICES = [
        ('Yes', 'Oui'),
        ('No', 'Non'),
    ]
    
    SPECIALISATION_MBA_CHOICES = [
        ('Mkt&HR', 'Marketing & RH'),
        ('Mkt&Fin', 'Marketing & Finance'),
    ]
    
    # Attributs du dataset uniquement
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, verbose_name="Genre")
    secondary_education_p = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Secondary Education %"
    )
    education_board_type = models.CharField(max_length=10, choices=EDUCATION_BOARD_CHOICES, verbose_name="Education Board Type")
    higher_secondary_p = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Higher Secondary %"
    )
    h_education_board_type = models.CharField(max_length=10, choices=EDUCATION_BOARD_CHOICES, verbose_name="H Education Board Type")
    higher_secondary_specialization = models.CharField(max_length=20, choices=SPECIALISATION_CHOICES, verbose_name="Higher Secondary Specialization")
    degree_p = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Degree %"
    )
    degree_type = models.CharField(max_length=20, choices=DEGREE_TYPE_CHOICES, verbose_name="Degree Type")
    work_experience = models.CharField(max_length=3, choices=WORK_EXPERIENCE_CHOICES, verbose_name="Work Experience")
    etest_p = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Etest %"
    )
    specialisation = models.CharField(max_length=10, choices=SPECIALISATION_MBA_CHOICES, verbose_name="Specialisation")
    mba_p = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="MBA %"
    )
    
    # Résultats de prédiction
    probabilite_performance = models.FloatField(null=True, blank=True, verbose_name="Probabilité de performance (%)")
    prediction_performance = models.BooleanField(null=True, blank=True, verbose_name="Prédiction (Performant/Non performant)")
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Candidat"
        verbose_name_plural = "Candidats"
        ordering = ['-probabilite_performance', '-date_creation']
    
    def __str__(self):
        return f"Candidat #{self.id} - {self.genre} ({self.probabilite_performance:.2f}%)"
