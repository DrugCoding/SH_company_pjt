from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'constructions/index.html')

def create(request):
    return render(request, 'constructions/create.html')