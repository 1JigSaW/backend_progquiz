from django.urls import path, include
from . import views

urlpatterns = [
    path('qualifications/', views.QualificationListView.as_view(), name='qualifications'),
]
