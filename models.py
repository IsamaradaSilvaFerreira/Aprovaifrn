from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Conteudo(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()

class Prova(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()

class Curso(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()

class Simulado(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()


class Matematica(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()

class Redacao(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()

class Linux(models.Model):
    photo = RichTextUploadingField()
    texto = RichTextField()
