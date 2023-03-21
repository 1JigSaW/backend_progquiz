from rest_framework import serializers
from app.models import *


class QualificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
