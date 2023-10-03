from django.urls import path
from . import views

urlpatterns = [
    path('criar_recibo/', views.criar_recibo, name='criar_recibo')
]
