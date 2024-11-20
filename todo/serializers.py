from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # creer le model serail 
    class Meta:
        model=Todo
        fields='__all__'