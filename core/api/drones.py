from .serializers import DroneSerializer, MedicationSerializer
from ..models import Drone, Medication
from  rest_framework.viewsets import ModelViewSet
from  rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response


#Crud Drone
class DroneList(ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer



#Crud Medication
class MedicationList(ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationRetrieveDelete(RetrieveDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

