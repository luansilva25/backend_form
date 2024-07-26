from ..models import States
from ..serializers import StatesSerializer
from rest_framework.viewsets import ModelViewSet

class StatesViewSet(ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StatesSerializer

    
    
