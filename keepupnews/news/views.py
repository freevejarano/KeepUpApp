from django.shortcuts import render
from .models import News
from django.utils import timezone

# Show all of news records
def index(request):
    all_news = News.objects.all()
    return render(request, 'index.html', {'all_news':all_news})

# Show a specific new
def view(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new,
        'status': 200
    }
    return render(request, 'view.html', context)

# Return the insert page
def create(request):
    return render(request, 'create.html')

# Receive the information of a new and create a new object in DB
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
        "msg": "¡LA NOTICIA HA SIDO CREADA CON ÉXITO!"
    }
    return render(request, 'create.html', context)

# Show the information of a new to edit
def edit(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new
    }
    return render(request, 'edit.html', context)

# Receive the information to update the object
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
        'msg':'LA NOTICIA HA SIDO EDITADA',
    }
    return render(request, 'edit.html', context)

# Search the new and delete it
def delete(request, id):
    new = News.objects.get(id=id)
    new.delete()
    context = {
        'status': 200,
        'msg':'LA NOTICIA HA SIDO BORRADA',
        'new': {'image': 'https://www.colombianosune.com/sites/default/files/asociaciones/NO_disponible-43_7.jpg'}
    }
    return render(request, 'view.html', context)
