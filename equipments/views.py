from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment
from .forms import EquipmentForm

# Create your views here.
def index(request):
    return render(request, 'equipments/index.html')

@login_required
def create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            equipment_form = EquipmentForm(request.POST, request.FILES)
            if equipment_form.is_valid():
                equipment = equipment_form.save(commit=False)
                equipment.user = request.user
                equipment.save()
                return redirect('equipments:index')
        else:
            equipment_form = EquipmentForm()
        context = {
            'equipment_form': equipment_form, 
        }
        return render(request, 'equipments/form.html', context)
    else:
        return redirect(request, 'equipments:index')
    

