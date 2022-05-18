
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileHistoryView, name="fileHistoryView"),
    path('post-report/', views.addFileView, name="addFileView"),
    path('<int:id>/', views.singleFileView, name="singleFileView"),
]