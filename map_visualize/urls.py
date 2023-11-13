from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('prac',views.prac, name='practice'),
]