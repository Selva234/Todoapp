from django.shortcuts import render


# create your views here.
def home(request):
    return render(request, 'main/index.html')


def add_todo(request):
    print(request)
