from django.urls import path
from . import views

app_name = "store"
  
urlpatterns = [
    path('', views.HomeView.as_view(), name="HomeView"),
    path('create-gig/', views.ManageGigView.as_view(), name="ManageGigView"),
]