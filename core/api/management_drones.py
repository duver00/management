from ..models import Drone, Medication
from .serializers import DroneSerializer, MedicationSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .utils import LimitWeight, BatteryLow, AuditBatteryLogger



@api_view(['GET'])
def IddleDrones(request) -> bool:
    if request.method== 'GET':
        drones = Drone.objects.filter(state__exact="IDDLE")
        if drones.count()>0:
            serializer = DroneSerializer(drones,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return NotFound()



@api_view(['GET'])
def CheckBattery(request,pk):
    if request.method== 'GET':
        try:
            drone = Drone.objects.get(pk=pk)
            return Response(data={"battery level": drone.battery_capacity,
                                  "serial_drone":drone.serial_number,
                                  "model":drone.model
                                  }, status=status.HTTP_200_OK)
        except:
            raise NotFound()



@api_view(['GET'])
def CheckMedication(request,pk):
    if request.method== 'GET':
        try:
            drone = Drone.objects.get(pk=pk)
            medication = DroneSerializer(drone)
            return Response(data={
                                  "Medications on drone":medication.data.get('medication')
                                  }, status=status.HTTP_200_OK)
        except:
            raise NotFound()



@api_view(['PUT'])
def LoadMedication(request,pk):
    if request.method == 'PUT':
        try:
            drone = Drone.objects.get(pk=pk)
        except Drone.DoesNotExist:
            raise NotFound()     
        drone.state = "LOADING"

        drone.save()
        if BatteryLow(drone):

            medications= []

            for medications_id in request.data.get('medication'):
                try:
                    medication = Medication.objects.get(pk=medications_id)
                    medications.append(medication)
                except:
                    raise NotFound()
                
            drone.medication.set(medications)           

            if LimitWeight(drone,request):
                drone.state = "LOADED"
                drone.save()
                drone_charged = DroneSerializer(drone)
                return Response(data={'msg':'Drone charged',
                                     'drone':drone_charged.data}, status=status.HTTP_200_OK)
              
            else :
                drone.state = "IDDLE"
                drone.medication.set([])
                drone.save()
                drone_iddle = DroneSerializer(drone)
                return Response(data={'error':'Medications exceed weight limit',
                                    'drone':drone_iddle.data},status=status.HTTP_400_BAD_REQUEST)
        else:
               return Response(data={'Battery Low':"Please charge drone's battery"},status=status.HTTP_400_BAD_REQUEST)







