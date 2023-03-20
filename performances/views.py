from django.shortcuts import render

# Create your views here.
def example(request):
    return render(request, 'performances/example.html')

def result(request):
    return render(request, 'performances/result.html')    