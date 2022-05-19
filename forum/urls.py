from django.urls import path
from . import views

urlpatterns = [
   path('', views.forumView, name="forumView"),
   path('<int:id>/', views.postView, name="postView"),
]