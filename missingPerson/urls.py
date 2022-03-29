from django.urls import path
from . import views

urlpatterns = [
   path('', views.missingPerson, name="missingPerson")
]
