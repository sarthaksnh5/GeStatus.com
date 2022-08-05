from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class MachineUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    deviceno = models.CharField(max_length=200)
    genset_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    time_at = models.TimeField(auto_now_add=True)
    low_oil = models.BooleanField(default=False)
    high_engine = models.BooleanField(default=False)
    low_fuel = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
    
class machineVI(models.Model):
    mac = models.ForeignKey(MachineUser, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    time_at = models.TimeField(auto_now_add=True)
    rh = models.FloatField()
    sh = models.FloatField()
    vr = models.FloatField()
    vy = models.FloatField()
    vb = models.FloatField()
    vry = models.FloatField()
    vyb = models.FloatField()
    vbr = models.FloatField()
    dgr = models.FloatField()
    dgy = models.FloatField()
    dgb = models.FloatField()
    dgry = models.FloatField()
    dgyb = models.FloatField()
    dgbr = models.FloatField()    
    ir = models.FloatField()
    iy = models.FloatField()
    ib = models.FloatField()
    pf = models.FloatField()
    powr = models.FloatField()
    powy = models.FloatField()
    powb = models.FloatField()
    apc = models.FloatField()
    apr = models.FloatField()
    apy = models.FloatField()
    apb = models.FloatField()
    kwh = models.FloatField()
    trhr = models.FloatField()    

class uiElement(models.Model):
    mac = models.ForeignKey(MachineUser, on_delete=models.CASCADE)
    speed = models.IntegerField()
    coolant = models.IntegerField()
    oilTemp = models.IntegerField()
    voltage = models.FloatField()
    fuel = models.FloatField()
    oilPress = models.FloatField()