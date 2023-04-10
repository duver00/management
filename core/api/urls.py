from django.urls import path, include
from .drones import DroneList, MedicationList,DroneRetrieveDestroy,MedicationRetrieveDelete
from .management_drones import IddleDrones,CheckBattery,CheckMedication, LoadMedication
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    #CRUD Drones
    path('drones/',DroneList.as_view(),name='list-drones' ),
    path('drone/<int:pk>',DroneRetrieveDestroy.as_view(),name='rud-drones' ),

    #Crud Medications
    path('medications/', MedicationList.as_view(),name='list-medications'),
    path('medication/<int:pk>',MedicationRetrieveDelete.as_view(), name='rud-medications'),

    #Load Drones
    path('drones/iddle/', IddleDrones,name='iddle'),

    #Check Battery of Drone
    path('drone/<int:pk>/battery',CheckBattery,name='check-battery'),

    #Check Medication on Drone
    path('drone/<int:pk>/medication',CheckMedication,name='check-battery'),

    #Loadind Drone with Medication
    path('drone/<int:pk>/load',LoadMedication,name='load-drone'),

]