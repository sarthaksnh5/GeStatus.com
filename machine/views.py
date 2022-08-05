from django.http.response import HttpResponse
from machine.models import MachineUser, machineVI, uiElement
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import json
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def base(request):
    try:
        dataMachine = MachineUser.objects.filter(user_id = request.user.id)
    except:
        dataMachine = ""

    context = {"data":dataMachine}
    return render(request, 'machine.html', context)


def registerMachine(request):    
    if request.method == "POST":
        newUser = request.user
        deviceno = request.POST['deviceno']
        gensetno = request.POST['gensetno']
        location = request.POST['location']

        newForm = MachineUser(user=newUser, deviceno=deviceno,
                              genset_no=gensetno, location=location)
        newForm.save()
        return redirect('base')


    context= {}

    return render(request, 'machine_register.html', context)

def machineDetails(request, pk):

    machineData = MachineUser.objects.get(id=pk)
    page = request.GET.get('page', 1)

    try:
        viDatad = machineVI.objects.filter(mac_id=pk)
    except:
        viDatad = ""

    try:
        uiData = uiElement.objects.filter(mac_id=pk)
    except:
        uiData = ""

    paginator = Paginator(viDatad, 10)

    try:
        viData = paginator.page(page)
    except PageNotAnInteger:
        viData = paginator.page(1)
    except EmptyPage:
        viData = paginator.page(paginator.num_pages)

    context = {'vi':viData, 'uiData':uiData, 'mac':machineData}
    return render(request, 'singleMachine.html', context)


def machineData(request):
    if request.method == "POST":
        data = request.body.decode("utf-8")
        jsonData = json.loads(data)
        print("Mach id: ")
        print(jsonData["mach_id"])
        try:
            machineVI.objects.get(mac_id = jsonData["mach_id"])
            getData = 1
        except:
            getData = 0
        print(getData)

        if getData:
            machineVI.objects.filter(mac_id=jsonData["mach_id"]).update(
                vr=jsonData["mainFreq"],
                vy=jsonData["L1NVolt"],
                vb=jsonData["L2NVolt"],
                vry=jsonData["L3NVolt"],
                ir=jsonData["G1NVolt"],
                iy=jsonData["G2NVolt"], 
                ib=jsonData["G3NVolt"],
                pf=jsonData["G1Curr"], 
                power=jsonData["G2Curr"],
                kwh=jsonData["G3Curr"],
                trhr=jsonData["CTemp"],
                vbr=jsonData["Batt"],
                vyb=jsonData["KWOVL"]
            )
            return HttpResponse("1")
        else:
            newForm = machineVI(
                mac_id=jsonData["mach_id"],
                vr=jsonData["mainFreq"],
                vy=jsonData["L1NVolt"],
                vb=jsonData["L2NVolt"],
                vry=jsonData["L3NVolt"],
                ir=jsonData["G1NVolt"],
                iy=jsonData["G2NVolt"], 
                ib=jsonData["G3NVolt"],
                pf=jsonData["G1Curr"], 
                power=jsonData["G2Curr"],
                kwh=jsonData["G3Curr"],
                trhr=jsonData["CTemp"],
                vyb=jsonData["Batt"],
                vbr=jsonData["KWOVL"]
            )
            newForm.save()
            return HttpResponse("11")

    return HttpResponse("Noo")

def likeData(request, pk, pk1, pk2, pk3):
    #if request.method == "GET":
    mac_id = pk
    type = pk1
    start = pk2
    end = pk3

    print(type, start, end, mac_id)
    newData = []
    queryNew = machineVI.objects.filter(created__range=[str(start),str(end)], mac_id=mac_id).values(type, "created")
    for data in queryNew:
        newData.append((data[type], str(data["created"])))
    
    return HttpResponse(newData)