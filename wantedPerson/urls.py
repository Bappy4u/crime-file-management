from django.urls import path
from . import views

urlpatterns = [
   path('', views.wantedPersonView, name="wantedPerson"),
   path('<int:id>/', views.personDetView, name="personDetView"),

]