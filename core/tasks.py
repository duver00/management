from .models import Drone
import logging
import datetime
from celery import shared_task

logger = logging.getLogger('battery status')


@shared_task
def StatusBattery():
  drones = Drone.objects.all()
  for x in drones:
      logger.warning(f'Date {datetime.datetime.now()} -- Drone {x.serial_number} Battery Level {x.battery_capacity} %')
      