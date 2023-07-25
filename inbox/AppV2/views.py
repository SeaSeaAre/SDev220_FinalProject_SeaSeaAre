from django.shortcuts import render, redirect
# My import
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required # Login required to access private pages
from django.views.decorators.cache import cache_control # Destroy section after logout
from .models import Client
# Create your views here.

#Function to home (frontend)

def home(request):
    return render(request, "home.html")

#Function to inbox (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    return render(request, "inbox.html")# Function to create a new client

def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        ssn = request.POST.get('ssn')

        client = Client.objects.create(name=name, address=address, phone=phone, email=email, ssn="#",)
        client.save()

        return redirect('client_dashboard/')  # Redirect to the dashboard page after creating the client

    return render(request, 'create_client.html')  # Render the form page initially

# Function to display the client dashboard
def client_dashboard(request):
    clients = Client.objects.all().order_by('name')
    context = {'clients': clients}
    return render(request, 'dashboard.html', context)