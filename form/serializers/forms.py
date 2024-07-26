from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Forms
from uploader.models import Image
from uploader.serializers import ImageSerializer

class FormsReatrieveSerializer(ModelSerializer):
    perfil = ImageSerializer(required=False)
    class Meta:
        model = Forms
        fields = '__all__'
        depth = 1

class FormsCreateSerializer(ModelSerializer):
    perfil_attachment_key = SlugRelatedField(
        source = 'perfil',
        queryset = Image.objects.all(),
        slug_field= 'attachment_key',
        write_only = True,
        required = False
    )
    perfil = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Forms
        fields = '__all__'

