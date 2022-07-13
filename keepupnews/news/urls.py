from django.urls import path
from . import views

# All of these are the availables paths in the web app
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('view/<int:id>', views.view, name='view')
]
