
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "nome",
                    models.CharField(max_length=100)
                ),
            ],
        ),

        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "titulo",
                    models.CharField(max_length=150)
                ),
                (
                    "descricao",
                    models.TextField(blank=True)
                ),
                (
                    "prioridade",
                    models.CharField(
                        max_length=10,
                        choices=[
                            ("BAIXA", "Baixa"),
                            ("MEDIA", "Média"),
                            ("ALTA", "Alta")
                        ],
                        default="MEDIA"
                    )
                ),
                (
                    "data_prevista",
                    models.DateField()
                ),
                (
                    "situacao",
                    models.CharField(
                        max_length=10,
                        choices=[
                            ("PENDENTE", "Pendente"),
                            ("CONCLUIDA", "Concluída")
                        ],
                        default="PENDENTE"
                    )
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tarefas.categoria"
                    )
                ),
            ],
        ),
    ]
