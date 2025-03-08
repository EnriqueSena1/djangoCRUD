from rest_framework import viewsets
from api.models import *
from api.serializers import *
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
