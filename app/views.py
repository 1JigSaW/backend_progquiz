from rest_framework import generics

from app.serializers import *
from app.models import *


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer


class SubgroupListView(generics.ListAPIView):
    serializer_class = SubgroupListSerializer

    def get_queryset(self):
        group_id = self.kwargs['group']
        return Subgroup.objects.filter(group_id=group_id)


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelListSerializer


class QuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsListSerializer

    def get_queryset(self):
        group_id = self.kwargs['group']
        subgroup_id = self.kwargs['subgroup']
        level_id = self.kwargs['level']
        return Questions.objects.filter(group_id=group_id)\
            .filter(subgroup_id=subgroup_id)\
            .filter(level_id=level_id)
