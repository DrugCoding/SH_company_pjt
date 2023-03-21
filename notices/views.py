from django.shortcuts import render, redirect, get_object_or_404
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
            notice.user = request.user
            notice.save()
            messages.success(request, '공지 글 작성이 완료되었습니다.')
            return redirect('notices:index')
    else:
        notice_form = NoticeForm()
    context = {
        'notice_form': notice_form,
    }
    return render(request, 'notices/form.html', context=context)

def detail(request,pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice_form = NoticeForm()
    # template에 객체 전달
    context = {
        'notice':notice,    
    }
    return render(request, 'notices/detail.html', context)