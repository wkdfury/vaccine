from django.db import models

# Create your models here.
class Slot(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    uid = models.IntegerField()
    vaccine = models.CharField(max_length=50)
    dose = models.TextField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def Slot_id(self):
        return self.id