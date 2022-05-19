from django.urls import path
from . import views

urlpatterns = [
   path('', views.announcementView, name="announcementv"),
   path('<int:id>/', views.singleNoticeView, name="singleNoticeView"),
]