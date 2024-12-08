from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Todo.

    Ce sérialiseur permet de transformer un objet Todo en JSON et inversement.
    """
    # creer le model serail 
    class Meta:
        model=Todo
        fields='__all__'

        # Si tu veux ajouter des descriptions personnalisées pour chaque champ, tu peux le faire ici.
        extra_kwargs = {
            'title': {'help_text': 'Le titre du todo, une description courte de la tâche.'},
            'completed': {'help_text': 'Indique si le todo est terminé ou non (true/false).'},
        }