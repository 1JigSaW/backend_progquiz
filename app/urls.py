from django.urls import path, include
from . import views

urlpatterns = [
    path('group/', views.GroupListView.as_view(), name='group'),
    path('subgroup/<int:group>', views.SubgroupListView.as_view(), name='subgroup'),
    path('questions/<int:group>/<int:subgroup>/<int:level>', views.QuestionsListView.as_view(), name='question'),
    path('levels/', views.LevelListView.as_view(), name='levels'),
]
