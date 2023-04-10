import re

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Drone(models.Model):
    STATE = [
        ('IDDLE','iddle'),
        ('LOADING','loading'),
        ('LOADED','loaded'),
        ('DELIVERING','delivering'),
        ('DELIVERED', 'delivered'),
        ('RETURNING','returning'),
    ]

    MODEL = [
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),

    ]

    serial_number = models.CharField(max_length=100)
    model =models.CharField(choices=MODEL, max_length=25)
    weight_limit = models.PositiveIntegerField(validators=
                                               [MinValueValidator(0),MaxValueValidator(500)],default=500)
    battery_capacity = models.PositiveSmallIntegerField(validators=
                                                        [MinValueValidator(0),MaxValueValidator(100)])
    state = models.CharField(choices=STATE,max_length=25, default="IDDLE")
    medication = models.ManyToManyField("Medication",related_name="medications",blank=True)

    class Meta:
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return self.serial_number +"  " + self.model+ " " + self.state




class Medication(models.Model):
    name = models.CharField(max_length=100, validators=[RegexValidator(
        regex='[a-zA-Z0-9_-]',message=
        "The code must has upper letter,"
        " number,underscore, middlescore")])
    weight = models.PositiveSmallIntegerField()
    code = models.CharField(validators=[RegexValidator(
        regex='[A-Z0-9_]',message=
        "The code must has upper letter,"
        " number and underscore")],max_length=255)
    image = models.ImageField(upload_to="media", null=True,blank=True)



    class Meta:
        verbose_name = "Medication"
        verbose_name_plural = "Medications"

    def __str__(self):
        return self.name
