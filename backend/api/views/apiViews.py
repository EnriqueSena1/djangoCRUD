from rest_framework import viewsets, status
from django.contrib.auth import authenticate, login
from api.models import *
from api.serializers import *
from rest_framework.response import Response

from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


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