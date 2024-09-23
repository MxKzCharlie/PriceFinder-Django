from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_api),
    path('', views.default_view)
]