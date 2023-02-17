from rest_framework.serializers import ModelSerializer
from .models import Cafes


class CafeSerializer(ModelSerializer):
    class Meta:
        model = Cafes
        fields = ['name', 'rating', 'location']