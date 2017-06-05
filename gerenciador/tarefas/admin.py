from django.contrib import admin
from tarefas.models import Usuario, Projeto, ProjetoUsuario, Tarefa
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(ProjetoUsuario)
admin.site.register(Tarefa)