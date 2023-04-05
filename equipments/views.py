from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment, EquipImage
from .forms import EquipmentForm, EquipImageForm

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
            equip_image_form = EquipImageForm(request.POST, request.FILES)
            tmp_img = request.FILES.getlist('equip_img')

            if equipment_form.is_valid() and equip_image_form.is_valid():
                equipment = equipment_form.save(commit=False)
                equipment.user = request.user

                if tmp_img:
                    for img in tmp_img:
                        img_instance = EquipImage(equipment=equipment, equip_img=img)
                        equipment.save()
                        img_instance.save()

                equipment.save()
                return redirect('equipments:index')
        else:
            equipment_form = EquipmentForm()
            equip_image_form = EquipImageForm()

        context = {
            'equipment_form': equipment_form, 
            'equip_image_form': EquipImageForm()
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
    equip_images = EquipImage.objects.filter(pk=equipment_pk)

    if request.user.is_superuser:
        if request.method == 'POST':
            equipment_form = EquipmentForm(request.POST, request.FILES, instance=equipment)
            # form에 equip_image 폼 추가
            equip_image_form = EquipImageForm(request.POST, request.FILES)
            tmp_img = request.FILES.getlist('equip_img')
                    
            for img in equip_images:
                if img:
                    img.delete()

            # 장비 및 장비 이미지 작성에 대한 폼이 유효하면
            if equipment_form.is_valid() and equip_image_form.is_valid():
                
                if tmp_img:
                    for img in tmp_img:
                        img_instance = EquipImage(equipment=equipment, equip_img=img)
                        equipment.save()
                        img_instance.save()

                equipment_form.save()
                return redirect("equipments:detail", equipment_pk)
        else:
            equipment_form = EquipmentForm(instance=equipment)
            if equip_images:
                equip_image_form = EquipImageForm(instance=equip_images[0])
            else:
                equip_image_form = EquipImageForm()
        context = {
            "equipment_form": equipment_form, 
            "equipment": equipment,
            "equip_image_form": equip_image_form,
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
