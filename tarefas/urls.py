from django.urls import path
from . import views
app_name = 'tarefas'
urlpatterns = [
    path('', views.lista, name='lista'),
    path('tarefas/', views.lista, name='lista_tarefas'),
    path('tarefas/nova/', views.criar, name='criar'),
    path('tarefas/<int:pk>/editar/', views.editar, name='editar'),
    path('tarefas/<int:pk>/concluir/', views.concluir, name='concluir'),
    path('tarefas/<int:pk>/excluir/', views.excluir, name='excluir'),
]
