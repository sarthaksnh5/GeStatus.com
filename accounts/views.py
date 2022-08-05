from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
