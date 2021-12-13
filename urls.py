from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.index),
    path('provas/', views.pro),
    path('conteudos/', views.conteudos),
    path('Cursos', views.cursos),
    path('simulados/', views.simul),
    path('disciplinas/', views.Matema),
    path('Redacaos/', views.Redac),


]+ static(settings.MEDIA_URL, documento_root=settings.MEDIA_ROOT)