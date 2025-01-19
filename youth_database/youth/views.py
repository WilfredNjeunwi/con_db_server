from rest_framework import viewsets
from .models import Youth
from .serializers import YouthSerializer

class YouthViewSet(viewsets.ModelViewSet):
    queryset = Youth.objects.all()
    serializer_class = YouthSerializer