from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment
from .forms import EquipmentForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    equipments = Equipment.objects.order_by('-pk')
    context = {
        "equipments": equipments,
    }
    return render(request, 'equipments/index.html', context)

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
    
def detail(request, equipment_pk):
    equipment = Equipment.objects.get(pk=equipment_pk)
    context = {
        'equipment': equipment,
    }
    return render(request, 'equipments/detail.html', context)

@login_required
def update(request, equipment_pk):
    equipment = Equipment.objects.get(pk=equipment_pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            equipment_form = EquipmentForm(request.POST, request.FILES, instance=equipment)
            if equipment_form.is_valid():
                equipment_form.save()
                return redirect("equipments:detail", equipment_pk)
        else:
            equipment_form = EquipmentForm(instance=equipment)
        context = {
            "equipment_form": equipment_form, 
            "equipment": equipment,
        }
        return render(request, "equipments/form.html", context)
    else:
        return redirect("equipments:detail", equipment_pk)


@login_required
def delete(request, equipment_pk):
    if request.user.is_authenticated and request.user.is_superuser:
        equipment = Equipment.objects.get(pk=equipment_pk)
        equipment.delete()
        return redirect("equipments:index")

# # 검색 기능 - 요청 url 에 keyword 정보가 있는지 확인하고, 해당 키워드를 가지고 title 필드를 검색해서 키워드가 포함된 객체만 notices 에 담겨진다.
# def search(request):
#     keyword = request.GET.get("keyword", "")  # 검색어

#     if keyword:
#         equipments = Equipment.objects.filter(
#             Q(title__icontains=keyword) | Q(content__icontains=keyword) # Q는 장고 model orm으로 where 절에 or문을 추가하고 싶을 때 사용
#         ).distinct()
        
#         context = {
#             "equipments": equipments,
#             "keyword": keyword,
#         }
#         return render(request, "equipments/search.html", context)
#     else:
#         return redirect("equipments:index")
