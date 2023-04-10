from ..models import Drone, Medication
from ..tasks import StatusBattery



def BatteryLow(obj):
    
    if int(obj.battery_capacity) < 25:
        print('false')
        return False
    return True
    

def LimitWeight(obj,request):
    total=0
    for x in request.data.get('medication'):
      med = Medication.objects.get(pk=x)
      total += med.weight
    if obj.weight_limit < total:
       return False
    return True



def AuditBatteryLogger():
   StatusBattery.delay()

