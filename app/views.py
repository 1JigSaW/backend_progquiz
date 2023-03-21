from rest_framework import generics

from app.serializers import QualificationListSerializer
from app.models import *


class QualificationListView(generics.ListAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationListSerializer
