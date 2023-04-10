from rest_framework import serializers
from ..models import Drone,Medication




class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = "__all__"



class DroneSerializer(serializers.ModelSerializer):
  #  medication = MedicationSerializer(many=True)

    class Meta:
        model= Drone
        fields = "__all__"
        depth = 1









