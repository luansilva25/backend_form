from ..models import ProgLang
from rest_framework.serializers import ModelSerializer

class ProgLangSerializer(ModelSerializer):
    class Meta:
        model = ProgLang
        fields = '__all__'