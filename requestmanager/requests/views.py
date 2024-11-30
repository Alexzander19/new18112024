from .models import Request
from .forms import RequestForm
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def create_request(request):

    if request.method != 'POST':
        # данные не отправлялись - создается пустая форма.
        form = RequestForm()
    else:
        # отправлены данные POST. Обработать данные.
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list.html')
        
    # вывести пустую или недействительную форму.
    context = {'form': form}

    return render(request,'create_request.html',context)

def request_list(request):
    request_list = Request.objects.all()
    context = {'list': request_list}
    return render(request,"request_list.html",context)

def one_request(request, request_id):
    # response = "Вы смотрите каждый блог по отдельности %s."
    one_request = Request.objects.get(id = request_id)
    context = {"one_request": one_request}
   
    # return HttpResponse(response % blog_id)
    return render(request, "one_request.html", context)   

