from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pno = request.POST.get('pno')
        print(f"The name of the customer is{name}")
        print(f"The email of the customer is {pno}")
        print(f"The pno of the customer is {pno}")
        return HttpResponse("go and check in the console...")
    return render(request,'register.html')