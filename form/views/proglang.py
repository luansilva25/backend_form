from ..serializers import ProgLangSerializer
from ..models import ProgLang
from rest_framework.viewsets import ModelViewSet

class ProgLangViewSet(ModelViewSet):
    queryset = ProgLang.objects.all()
    serializer_class = ProgLangSerializer
