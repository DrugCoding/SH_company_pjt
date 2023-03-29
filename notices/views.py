from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice, Photo
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def index(request):
    notices = Notice.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(notices, 5)
    paginated_notices = paginator.get_page(page)
    max_index = len(paginator.page_range)
    context = {
        'notices': notices,
        "paginated_notices": paginated_notices,
        "max_index": max_index,
    }
    return render(request, 'notices/index.html', context)

@login_required
def create(request):
    if request.user.is_superuser: # 관리자만 작성 가능
        if request.method == "POST":
            notice_form = NoticeForm(request.POST, request.FILES) # 이미지는 request.FILES로 받는다.
            if notice_form.is_valid():
                notice = notice_form.save(commit=False) #  form이 작동하고 나서 save가 작동하도록 한다.
                notice.user = request.user
                notice.save()
                for img in request.FILES.getlist('imgs'):
                    # Photo 객체를 하나 생성한다.
                    photo = Photo()
                    # 외래키로 현재 생성한 Post의 기본키를 참조한다.
                    photo.notice = notice
                    # imgs로부터 가져온 이미지 파일 하나를 저장한다.
                    photo.image = img
                    # 데이터베이스에 저장
                    photo.save()
                return redirect('notices:index')
        else:
            notice_form = NoticeForm()
        context = {
            'notice_form': notice_form,
        }
        return render(request, 'notices/form.html', context=context)
    else:
        return redirect('notices:index')

def detail(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    # template에 객체 전달
    context = {
        'notice':notice,    
    }
    response = render(request, 'notices/detail.html', context)
    
    # 쿠키 이용한 조회수 기능
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookievalue = request.COOKIES.get("hitnotice", "")

    if f"{notice_pk}" not in cookievalue:
        cookievalue += f"{notice_pk}"
        response.set_cookie(
            "hitnotice", value=cookievalue, max_age=max_age, httponly=True
        )
        notice.hits += 1
        notice.save()
    return response

@login_required
def update(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    # image = notice.photo_set.all()
    if request.user.is_superuser: # 관리자만 수정 가능
        if request.method == 'POST':
            notice_form = NoticeForm(request.POST, request.FILES, instance=notice)
            if notice_form.is_valid():
                notice_form.save()
                for img in request.FILES.getlist('imgs'):
                    # Photo 객체를 하나 생성한다.
                    photo = Photo()
                    # 외래키로 현재 생성한 Post의 기본키를 참조한다.
                    photo.notice = notice
                    # imgs로부터 가져온 이미지 파일 하나를 저장한다.
                    photo.image = img
                    # 데이터베이스에 저장
                    photo.save()
                    
                return redirect("notices:detail", notice_pk)
        else:
            # GET : Form을 제공
            notice_form = NoticeForm(instance=notice)
        context = {
            "notice_form": notice_form,
            "notice": notice, # notice를 context에 넘겨 줘야 수정하는 form에서 기존 작성한 것들이 보임!
        }
        return render(request, 'notices/form.html', context)
    else:
        return redirect("notices:detail", notice_pk)

@login_required
def delete(request, notice_pk):
    if request.user.is_authenticated and request.user == notice.user:
        notice = Notice.objects.get(pk=notice_pk)
        notice.delete()
        return redirect("notices:index")
    

# 검색 기능 - 요청 url 에 keyword 정보가 있는지 확인하고, 해당 키워드를 가지고 title 필드를 검색해서 키워드가 포함된 객체만 notices 에 담겨진다.
def search(request):
    keyword = request.GET.get("keyword", "")  # 검색어

    if keyword:
        notices = Notice.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword) # Q는 장고 model orm으로 where 절에 or문을 추가하고 싶을 때 사용
        ).distinct()
        
        context = {
            "notices": notices,
            "keyword": keyword,
        }
        return render(request, "notices/search.html", context)
    else:
        return redirect("notices:index")