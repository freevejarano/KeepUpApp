from django.shortcuts import render
from .models import News

def index(request):
    all_news = News.objects.all()

    return render(request, 'index.html', all_news)