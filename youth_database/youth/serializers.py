from rest_framework import serializers
from .models import Youth

class YouthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youth
        fields = '__all__'