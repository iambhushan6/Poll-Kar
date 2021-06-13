from django.urls import path, include
from main import views

urlpatterns = [

    path('', views.allpolls, name= 'allpolls' ),

    path('mypolls/', views.mypolls, name= 'mypolls' ),

    path('create/', views.create, name= 'create' ),

    path('vote/<int:pk>', views.vote, name= 'vote' ),

    path('results/<int:pk>', views.results, name= 'result' ),
]