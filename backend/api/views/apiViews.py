from rest_framework import viewsets, status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

class User(APIView):
    def get(self, request, id=None):

        if id:
            usuario = get_object_or_404(CustomUser,pk=id)
            serializers = UserSerializer(usuario)
            return Response(serializers.data, status=status.HTTP_200_OK)

        usuario = CustomUser.objects.all()
        serializers = UserSerializer(usuario, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self,request):
        nome = request.data.get('username')
        senha = request.data.get('password')

        if not nome or not senha:
            return Response({"error": "Todos os campos são obrigadotorios."}, status=status.HTTP_400_BAD_REQUEST)
        
        usuario = CustomUser.objects.create(
            username=nome,
            password=make_password(senha),
            is_active=True,
            is_aluno=True
        )
        return Response({"message": "Usuario criado com sucesso!", "id":
                         usuario.id}, status=status.HTTP_201_CREATED)
    
    def put(self,request,id):
        usuario = get_object_or_404(CustomUser, pk=id)
        serializers = UserSerializer(usuario, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        return Response(serializers.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        usuario = get_object_or_404(CustomUser, pk=id)
        if usuario:
            usuario.delete()
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"status": status.HTTP_404_NOT_FOUND})

class Login(APIView):
    def post(self, resquest):
        nome = resquest.data.get("nome")
        senha = resquest.data.get("senha")


        usuario = authenticate(username=nome,password=senha)

        if (usuario):
            login(resquest,usuario)
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"mensagem": "usuario não encontrado", "status": status.HTTP_401_UNAUTHORIZED})
        
