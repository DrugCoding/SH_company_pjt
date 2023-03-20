from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'companies/index.html')

def greeting(request):
    return render(request, 'companies/greeting.html')
    
def history(request):
    return render(request, 'companies/history.html')

def patent(request):
    return render(request, 'companies/patent.html')

def come(request):
    return render(request, 'companies/come.html')