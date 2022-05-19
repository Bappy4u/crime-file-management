from django.urls import path
from . import views

urlpatterns = [
   path('', views.missingPerson, name="missingPerson"),
   path('pending/', views.pendingMissingPerson, name="pendingMissingPerson"),
   path('add/', views.addMissingPerson, name='addMissing'),
   path('<int:id>/', views.missingPersonDet, name="missingPersonDet"),
]
