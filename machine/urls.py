from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('regsiterMachine', views.registerMachine, name="regsiterMachine"),
    path('singleMachine/<str:pk>', views.machineDetails, name="singleMachine"),
    path('addMachineData/', views.machineData),
    path('singleMachine/likeData/<str:pk>/<str:pk1>/<str:pk2>/<str:pk3>', views.likeData, name='likeData'),
]
