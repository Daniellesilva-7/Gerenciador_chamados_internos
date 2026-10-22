from django.contrib import admin
from .models import Categoria, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "categoria",
        "prioridade",
        "situacao",
        "data_prevista",
        "responsavel"
    )

    list_filter = (
        "situacao",
        "prioridade",
        "categoria",
        "responsavel"
    )

    search_fields = ("titulo", "descricao")
    ordering = ("data_prevista",)
