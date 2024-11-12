from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, BookHotelTicket, BookZooTicket
from .models import Record, BookingHotel, BookingZoo
from datetime import datetime
from datetime import timedelta
from datetime import timezone

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
    context = {'form': form}

    if request.method == "POST":
        form = BookHotelTicket(request.POST)
        if form.is_valid():
            # ad = request.POST.get('Arrival_date')
            # dd = request.POST.get('Departure_date')

            # print(dd)
            
            # print(overall_cost)
            # context = {"Arrival": ad, "Depart":dd, "overall_cost":overall_cost}

            # Calculate duration and cost if applicable
            # Arrival_date = form.cleaned_data['Arrival_date']
            # Departure_date = form.cleaned_data['Departure_date']
            # duration_in_days = (Departure_date - Arrival_date).days
            # ... Your logic to calculate duration and cost based on arrival_date and departure_date
            # rate_per_day = 100
            # total_cost = duration_in_days * rate_per_day
            # Pass calculated values (if any) to the template context
            # context.update({
            #     'duration_in_days': duration_in_days,  # Replace with your calculated value
            #     'total_cost': total_cost,            # Replace with your calculated value
            # })
            
            
            messages.success(request, "Ticket Booked, P Diddy on his way")
            print("saved")
            
            

            #context.update(data)
            form.save()

            return redirect('HotelConfirmation')
        else:
            print("What the sigma")
            print(form.errors)

    return render(request, 'website/hotel.html', context=context)

def zoo(request):
    return render(request, 'website/zoo.html')

def HotelConfirmation(request):
    HotelTicket = BookingHotel.objects.latest("customer_ID_id")
    Arrival_date = HotelTicket.Arrival_date
    Departure_date = HotelTicket.Departure_date
    new_variable = Departure_date-Arrival_date
    overall_cost = int(new_variable.days) * 70
    context = {'ticket': HotelTicket, 'overall_cost':overall_cost}
    if request.method == "POST":
        HotelTicket.Hotel_cost=overall_cost
        HotelTicket.save()
        messages.success(request, "Ticket Booked, P Diddy on his way")
    return render(request, 'website/HotelConfirmation.html', context)

def delete_bookingH(request):
    print("Message error")
    HotelTicket = BookingHotel.objects.latest("customer_ID_id")
    HotelTicket.delete()
    
    messages.error(request,"Your booking has been deleted. Please contact Elon at your earliest convenience.")
    return redirect(request,'')
    
    

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

    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")

#Dashboard -
@login_required(login_url='my-login')
def dashboard(request):
    if request.user.is_superuser:
        my_records = Record.objects.all()
        context = {'records': my_records}
        # print(context)
        return render(request, 'website/dashboard.html', context=context)
    else:
        messages.error(request, "YOU ARE NOT AUTHORISED TO ACCESS THIS PAGE")
        return redirect("")



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