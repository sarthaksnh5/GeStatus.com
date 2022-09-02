import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponse

from machine.models import MachineUser, machineVI, uiElement

# Create your views here.
def index(request):
    return render(request, "index.html")

def loginUser(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            form = login(request, user)
            return redirect('base')
        else:
            messages.info(request, "Error while login please try again")
            return redirect('loginUser')

    form = AuthenticationForm()
    form2 = UserCreationForm()
    context = {'form':form, 'form2':form2}
    return render(request, 'login.html', context)


def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created Successfully!!!")
        else:
            messages.info(request, form.errors)

        return redirect('loginUser')

def logout_view(request):
	logout(request)
	return redirect('loginUser')

def addMachineData(request):
    if request.method == 'POST':
        data = request.body.decode("utf-8")
        jsonData = json.loads(data)

        machine = MachineUser.objects.get(id=jsonData['mach_id'])
        
        uiElement(mac=machine,
            mains=jsonData['mains'],
            run_hour=jsonData['run_hour'],
            dg_kwh=jsonData['dg_kwh'],
            voltage=jsonData['voltage'],
            battery=jsonData['battery'],
            rpm=jsonData['speed'],
            oilTemp=jsonData['oilPress'],
            temperature=jsonData['temperature'],
            fuel=jsonData['fuel'],
            coolant=jsonData['CTemp'],
        ).save()

        machineVI(
            mac=machine,
            gen_freq=jsonData['gen_freq'],
            g1nvolt=jsonData['g1nvolt'],
            g2nvolt=jsonData['g2nvolt'],
            g3nvolt=jsonData['g3nvolt'],
            G1Curr=jsonData['G1Curr'],
            G2Curr=jsonData['G2Curr'],
            G3Curr=jsonData['G3Curr'],
            G1Watt=jsonData['G1Watt'],
            G2Watt=jsonData['G2Watt'],
            G3Watt=jsonData['G3Watt'],
            mainFreq=jsonData['mainFreq'],
            MainL1NVolt=jsonData['MainL1NVolt'],
            MainL2NVolt=jsonData['MainL2NVolt'],
            MainL3NVolt=jsonData['MainL3NVolt'],
            Main1Curr=jsonData['Main1Curr'],
            Main2Curr=jsonData['Main2Curr'],
            Main3Curr=jsonData['Main3Curr'],
            Main1Watt=jsonData['Main1Watt'],
            Main2Watt=jsonData['Main2Watt'],
            Main3Watt=jsonData['Main3Watt'],
            genpf1=jsonData['genpf1'],
            genpf2=jsonData['genpf2'],
            genpf3=jsonData['genpf3'],
            avggenpf=jsonData['avggenpf'],
            genkvar=jsonData['genkvar'],
        ).save()

    return HttpResponse("Noo")
