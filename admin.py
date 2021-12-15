from django.contrib import admin
from pagina.models import Conteudo, Prova, Curso, Simulado, Matematica, Redacao

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']

@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']

@admin.register(Simulado)
class SimuladoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']

@admin.register(Matematica)
class MatematicaAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']

@admin.register(Redacao)
class RedacaoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'texto']
