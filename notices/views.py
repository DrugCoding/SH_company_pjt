from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice
from django.contrib import messages

# Create your views here.
def index(request):
    notices = Notice.objects.order_by('-pk')
    context = {
        'notices': notices,
    }
    return render(request, 'notices/index.html', context)

def create(request):
    if request.method == "POST":
        notice_form = NoticeForm(request.POST, request.FILES) # 이미지는 request.FILES로 받는다.
        if notice_form.is_valid():
            notice = notice_form.save(commit=False) #  form이 작동하고 나서 save가 작동하도록 한다.
            # notice.user = request.user
            notice.save()
            messages.success(request, '공지 글 작성이 완료되었습니다.')
            return redirect('notices:index')
    else:
        notice_form = NoticeForm()
    context = {
        'notice_form': notice_form,
    }
    return render(request, 'notices/form.html', context=context)

def detail(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    # template에 객체 전달
    context = {
        'notice':notice,    
    }
    return render(request, 'notices/detail.html', context)

def update(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    if request.method == 'POST':
        notice_form = NoticeForm(request.POST, request.FILES, instance=notice)
        if notice_form.is_valid():
            notice_form.save()
            return redirect("notices:detail", notice_pk)
    else:
        # GET : Form을 제공
        notice_form = NoticeForm(instance=notice)
    context = {
        "notice_form": notice_form,
        "notice": notice, # notice를 context에 넘겨 줘야 수정하는 form에서 기존 작성한 것들이 보임!
    }
    return render(request, 'notices/form.html', context)
           

# 검색 기능 - 요청 url 에 keyword 정보가 있는지 확인하고, 해당 키워드를 가지고 title 필드를 검색해서 키워드가 포함된 객체만 notices 에 담겨진다.
def search(request):
    keyword = request.GET.get("keyword", "")  # 검색어

    if keyword:
        notices = Notice.objects.filter(title__icontains=keyword).values()
        
        context = {
            "notices": notices,
            "keyword": keyword,
        }
        return render(request, "notices/search.html", context)