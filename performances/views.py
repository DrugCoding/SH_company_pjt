from django.shortcuts import render, redirect
from .forms import PerformanceForm
from .models import Performance
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    p_articles = Performance.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(p_articles, 13) #한 페이지 당 몇개 씩 보여줄 지 지정 
    paginated_performances = paginator.get_page(page)
    max_index = len(paginator.page_range)
    context = {
        'p_articles': p_articles,
        'paginated_performances': paginated_performances,
        'max_index': max_index,
    }
    return render(request, 'performances/index.html', context)

def create(request):
    if request.user.is_superuser: # 관리자만 작성 가능
        if request.method == 'POST':
            p_form = PerformanceForm(request.POST)
            if p_form.is_valid():
                p_article = p_form.save(commit=False)
                p_article.user = request.user
                p_article.save()
                return redirect('performances:index')
        else:
            p_form = PerformanceForm()
        context = {
            'p_form': p_form
        }
        return render(request, 'performances/create.html', context)

def detail(request, p_pk):
    p_article = Performance.objects.get(pk=p_pk)
    context = {
        'p_article': p_article,
    }
    return render(request, 'performances/detail.html', context)

def update(request, p_pk):
    p_article = Performance.objects.get(pk=p_pk)
    if request.user.is_superuser: # 관리자만 수정 가능
        if request.method == 'POST':
            p_form = PerformanceForm(request.POST, instance=p_article)
            if p_form.is_valid():
                p_form.save()
                return redirect('performances:detail', p_pk)
        else:
            p_form = PerformanceForm(instance=p_article)
        context = {
            'p_form': p_form,
            'p_article': p_article,
        }
        return render(request, 'performances/create.html', context)

def delete(request, p_pk):
    p_article = Performance.objects.get(pk=p_pk)
    p_article.delete()
    return redirect('performances:index')