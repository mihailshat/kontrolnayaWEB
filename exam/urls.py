from django.urls import path
from . import views

urlpatterns = [
    path('msexam/', views.msexam_list, name='msexam_list'),
] 