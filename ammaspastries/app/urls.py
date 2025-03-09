from django.urls import path
from . import views

urlpatterns = [
    path("",views.display),
    path("theme",views.theme),
    path("cakes",views.cakes),
]