from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, BookHotelTicket, BookZooTicket
from .models import Record, BookingHotel, BookingZoo


# Create your views here.

def home(request):
    return render(request, 'website/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print("The method has been posted")
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('my-login')

    context = {'form':form}

    return render(request,'website/register.html',context=context)

def hotel(request):
    form = BookHotelTicket()
    context = {'form':form}
    return render(request, 'website/hotel.html',context=context)

def zoo(request):
    return render(request, 'website/zoo.html')

def safari(request):
    return render(request, 'website/safari.html')

# login a user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    context={'login_form':form}
    return render(request,'website/my-login.html',context=context)

#logout user

def user_logout(request):

    auth.logout(request.messages.success(request, "Logout success!"))
    return redirect("my-login")

#Dashboard -
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    # print(context)
    return render(request, 'website/dashboard.html', context=context)


#Create a record
@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'create_form': form}
    return render(request, 'website/create-record.html',context=context)

#Update a record
@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form= UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")
    
    context = {'update_form': form}
    return render(request, 'website/update-record.html',context=context)

#Read a single record
@login_required(login_url='my-login')
def singular_record(request,pk):

    one_record = Record.objects.get(id=pk)
    context = {'record':one_record}
    return render(request, 'website/view-record.html',context=context)

#Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect("dashboard")