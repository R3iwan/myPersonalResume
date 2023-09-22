from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exp/', views.exp, name='exp'),
    path('skills/', views.skills, name='skills'),
]
