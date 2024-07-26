from ..models import States
from rest_framework.serializers import ModelSerializer

class StatesSerializer(ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'