from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def list_todos(request):
    """
    Récupérer la liste de tous les todos.

    Cette API retourne tous les éléments Todo dans la base de données sous forme de liste.
    """
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_todo(request):
    """
    Ajouter un nouveau todo.

    Cette API permet de créer un nouveau todo. Les données doivent être envoyées
    dans le corps de la requête sous forme de JSON.
    """
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_todo(request, pk):
    """
    Mettre à jour un todo existant.

    Cette API permet de mettre à jour un todo avec un identifiant spécifique (pk).
    Le champ `completed` peut être mis à jour dans le corps de la requête.
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    
    if 'completed' in request.data:
        todo.completed = request.data['completed']
        todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    """
    Supprimer un todo existant.

    Cette API permet de supprimer un todo avec un identifiant spécifique (pk).
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response(status==status.HTTP_204_NO_CONTENT)