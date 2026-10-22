"""Mantém as tarefas antigas: use TAREFAS_USUARIO_LEGADO ou o admin único."""
import os
from django.conf import settings
from django.db import migrations

def atribuir(apps, schema_editor):
    Tarefa = apps.get_model('tarefas', 'Tarefa')
    banco = schema_editor.connection.alias
    antigas = Tarefa.objects.using(banco).filter(responsavel__isnull=True)
    if not antigas.exists():
        return
    Usuario = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    nome = os.environ.get('TAREFAS_USUARIO_LEGADO', '').strip()
    if nome:
        usuario = Usuario.objects.using(banco).filter(username=nome).first()
    else:
        administradores = list(Usuario.objects.using(banco).filter(is_superuser=True)[:2])
        usuario = administradores[0] if len(administradores) == 1 else None
    if usuario is None:
        raise RuntimeError('Crie um superusuário único ou defina TAREFAS_USUARIO_LEGADO antes de migrar.')
    antigas.update(responsavel_id=usuario.pk)

class Migration(migrations.Migration):
    dependencies = [('tarefas', '0002_responsavel_opcional')]
    operations = [migrations.RunPython(atribuir, migrations.RunPython.noop)]
