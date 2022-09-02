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
    machine_kv = models.CharField(max_length=200, default=45)
    machine_phase = models.CharField(max_length=200, default=1)
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
    gen_freq = models.FloatField()
    g1nvolt = models.FloatField()
    g2nvolt = models.FloatField()
    g3nvolt = models.FloatField()
    G1Curr = models.FloatField()
    G2Curr = models.FloatField()
    G3Curr = models.FloatField()
    G1Watt = models.FloatField()
    G2Watt = models.FloatField()
    G3Watt = models.FloatField()
    mainFreq = models.FloatField()
    MainL1NVolt = models.FloatField()
    MainL2NVolt = models.FloatField()
    MainL3NVolt = models.FloatField()
    Main1Curr = models.FloatField()
    Main2Curr = models.FloatField()
    Main3Curr = models.FloatField()
    Main1Watt = models.FloatField()
    Main2Watt = models.FloatField()
    Main3Watt = models.FloatField()
    genpf1 = models.FloatField()
    genpf2 = models.FloatField()
    genpf3 = models.FloatField()
    avggenpf = models.FloatField()
    genkvar = models.FloatField()
    

class uiElement(models.Model):
    mac = models.ForeignKey(MachineUser, on_delete=models.CASCADE)
    mains = models.FloatField()
    run_hour = models.FloatField()
    dg_kwh = models.FloatField()
    voltage = models.FloatField()
    battery = models.FloatField()
    rpm = models.IntegerField()
    oilTemp = models.IntegerField()
    temperature = models.FloatField()
    fuel = models.FloatField()
    coolant = models.IntegerField()
    