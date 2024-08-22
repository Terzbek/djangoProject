from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': "Главная страница под названием - Home",
        'list': ['first_user','second_user'],
        'dict': {'first_user': False, 'second_user':False},
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About page")
