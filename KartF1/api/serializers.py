from rest_framework.serializers import ModelSerializer
from .models import Kart

class KartSerializer(ModelSerializer):
    class Meta:
        model = Kart
        fields = '__all__'