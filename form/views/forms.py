from ..serializers import FormsReatrieveSerializer, FormsCreateSerializer
from ..models import Forms
from rest_framework.viewsets import ModelViewSet

class FormsViewSet(ModelViewSet):
    queryset = Forms.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return FormsCreateSerializer
        return FormsReatrieveSerializer
            