from django.urls import path
from .views import home, ramos, perfil

urlpatterns = [
    path('', home, name="home"),
    path('ramos/', ramos, name="ramos"),
    path('perfil/', perfil, name="perfil"),
]
