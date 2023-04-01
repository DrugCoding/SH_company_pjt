from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'constructions/index.html')

def create(request):
    return render(request, 'constructions/create.html')

def part01(request):
    return render(request, 'constructions/part01.html')
    
def part02(request):
    return render(request, 'constructions/part02.html')

def part03(request):
    return render(request, 'constructions/part03.html')

def part04(request):
    return render(request, 'constructions/part04.html')

def part05(request):
    return render(request, 'constructions/part05.html')

def part06(request):
    return render(request, 'constructions/part06.html')
    
def part07(request):
    return render(request, 'constructions/part07.html')

def part08(request):
    return render(request, 'constructions/part08.html')

def part09(request):
    return render(request, 'constructions/part09.html')