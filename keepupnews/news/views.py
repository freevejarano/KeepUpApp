from django.shortcuts import render
from .models import News
from django.utils import timezone

def index(request):
    all_news = News.objects.all()
    return render(request, 'index.html', {'all_news':all_news})

def create(request):
    return render(request, 'create.html')

def add(request):
    title = request.POST['title']
    image = request.POST['img']
    topic = request.POST['topic']
    description = request.POST['description']
    content = request.POST['content']
    new = News(title=title, image=image, topic=topic, date=timezone.now(), description=description, content=content)
    new.save()
    return render(request, 'create.html', {"status":200})

