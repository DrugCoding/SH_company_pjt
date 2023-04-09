from django.shortcuts import render, redirect
from .models import Construction, C_Category
from .forms import ConstructionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    c_articles = Construction.objects.all()

    c_article_item = Construction.objects.order_by("-pk")  # pk 순으로 정렬(등록한 것부터)
    paginator = Paginator(c_article_item, 8)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "c_articles": c_articles,
        "page_obj": page_obj,
    }
    return render(
        request, "constructions/index.html", context
    )  # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌

@login_required
def create(request):
    if request.user.is_superuser: # 관리자만 작성 가능
        if request.method == 'POST':
            c_form = ConstructionForm(request.POST, request.FILES)
            if c_form.is_valid():
                c_article = c_form.save(commit=False)
                c_article.user = request.user
                c_article.save()
                return redirect('constructions:index')
        else:
            c_form = ConstructionForm()
        context = {
            'c_form': c_form
        }
        return render(request, 'constructions/create.html', context)

def detail(request, c_pk):
    c_article = Construction.objects.get(pk=c_pk)
    context = {
        'c_article': c_article,
    }
    return render(request, 'constructions/detail.html', context)

def update(request, c_pk):
    c_article = Construction.objects.get(pk=c_pk)
    if request.user.is_superuser: # 관리자만 수정 가능
        if request.method == 'POST':
            c_form = ConstructionForm(request.POST, instance=c_article)
            if c_form.is_valid():
                c_form.save()
                return redirect('constructions:detail', c_pk)
        else:
            p_form = ConstructionForm(instance=c_article)
        context = {
            'c_form': c_form,
            'c_article': c_article,
        }
        return render(request, 'constructions/create.html', context)

def delete(request, c_pk):
    p_article = Construction.objects.get(pk=c_pk)
    p_article.delete()
    return redirect('performances:index')

def c_category(request, c_category_pk):
    try:
        category = C_Category.objects.get(pk=c_category_pk)
    except C_Category.DoesNotExist:
        category = None
    category_articles = Construction.objects.filter(c_list=category)
    paginator = Paginator(category_articles, 8)  # 정렬을 9개까지 보여줌
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "category_articles": category_articles,
        "page_obj": page_obj,
    }

    return render(request, "constructions/index.html", context)