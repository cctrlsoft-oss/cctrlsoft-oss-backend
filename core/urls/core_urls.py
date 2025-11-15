from django.urls import path
from core import views


urlpatterns = [
  path("perfil/", views.PerfilView.as_view(), name="perfil"),
  path("registro/", views.RegistroView.as_view(), name="registro"),
]