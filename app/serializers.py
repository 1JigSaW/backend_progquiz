from rest_framework import serializers
from app.models import *


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubgroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgroup
        fields = '__all__'


class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
