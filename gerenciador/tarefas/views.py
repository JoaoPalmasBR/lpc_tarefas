from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from tarefas.models import Usuario, Projeto, ProjetoUsuario, Tarefa

def index(request):
    html = """<h1>Tarefas</h1>
                <ul>
                    <li><a href='/usuario'>Usuarios</a></li>
                    <li><a href='/projeto'>Projetos</a></li>
                    <li><a href='/tarefa'>Tarefas</a></li>
                </ul>
            """
    return HttpResponse(html)
def listaUsuarios(request):
    html = "<h1>Lista de Usuarios</h1>"
    listaUsuario = Usuario.objects.all()
    for usuario in listaUsuario:
        html += '<ul type="none">'
        html += '<li><strong>{}</strong></li>'.format(usuario.nome)
        html += '<li>Email: {}</li>'.format(usuario.email)
        html += '<li>Senha: {}</li>'.format(usuario.senha)
        html += '</ul>'
        html += '<hr>'
    return HttpResponse(html)
def listaProjetos(request):
    html = "<h1>Lista de Projetos</h1>"
    html += '<ul type="none">'
    listaProjeto = Projeto.objects.all()
    for projeto in listaProjeto:
        html += '<li><strong>{}</strong></li>'.format(projeto.nome)
        html += '<hr>'
    html += '</ul>'
    return HttpResponse(html)
def listaProjetoUsuarios(request):
    html = "<h1>Lista de Projetos relacionados com Usuarios</h1>"
    html += '<ul type="none">'
    listaProjetoUsuario = ProjetoUsuario.objects.all()
    for projetousuario in listaProjetoUsuario:
        html += '<li>Projeto: <strong>{}</strong></li>'.format(projetousuario.projeto.nome)
        html += '<li>Usuario: <strong>{}</strong></li>'.format(projetousuario.usuario.nome)
        html += '<hr>'
    html += '</ul>'
    return HttpResponse(html)
def listaTarefas(request):
    html = "<h1>Lista de Tarefas</h1>"
    listaTarefa = Tarefa.objects.all()
    for tarefa in listaTarefa:
        html += '<ul type="none">'
        html += '<li><strong>{}</strong></li>'.format(tarefa.nome)
        html += '<li>Data de Inicio: <strong>{}</strong></li>'.format(tarefa.dataEHoraDeInicio)
        html += '<li>Usuario: <strong>{}</strong></li>'.format(tarefa.usuario.nome)
        html += '<li>Projeto: <strong>{}</strong></li>'.format(tarefa.projeto.nome)
        html += '</ul>'
        html += '<hr>'
    return HttpResponse(html)