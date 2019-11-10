from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request,'Labrinth/index.html')

def about_view(request):
    return render(request,'Labrinth/about.html')
