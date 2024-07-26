from rest_framework.serializers import ModelSerializer
from ..models import Hobbies

class HobbiesSerializer(ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'
        