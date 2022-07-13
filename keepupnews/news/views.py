from django.shortcuts import render
from .models import News
from django.utils import timezone

def index(request):
    all_news = News.objects.all()
    return render(request, 'index.html', {'all_news':all_news})

def view(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new
    }
    return render(request, 'view.html', context)

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
    context = {
        "status":200,
        "msg": "¡Noticia creada con éxito!"
    }
    return render(request, 'create.html', context)

def edit(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new
    }
    return render(request, 'edit.html', context)

def update(request, id):
    new = News.objects.get(id=id)
    new.title = request.POST['title']
    new.image = request.POST['img']
    new.topic = request.POST['topic']
    new.date = timezone.now()
    new.description = request.POST['description']
    new.content = request.POST['content']
    new.save()
    context = {
        'status': 200,
        'msg':'La noticia ha sido editada',
    }
    return render(request, 'edit.html', context)

def delete(request, id):
    new = News.objects.get(id=id)
    new.delete()
    context = {
        'status': 200,
        'msg':'La noticia ha sido borrada',
    }
    return render(request, 'view.html', context)
