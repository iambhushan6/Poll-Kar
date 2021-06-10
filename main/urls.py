from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name= 'home' ),

    path('create/', views.create, name= 'create' ),

    path('vote/<int:pk>', views.vote, name= 'vote' ),

    path('results/<int:pk>', views.results, name= 'result' ),
]