"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from biblioteca.settings import MEDIA_ROOT
from livro.api import viewsets as livroviewsets
from django.conf import settings
from django.conf.urls.static import static


route = routers.DefaultRouter()

route.register(r'livro', livroviewsets.LivroViewset, basename='Livro')

route.register(r'emprestimo', livroviewsets.EmprestimoViewset, basename='Emprestimo')

route.register(r'usuario', livroviewsets.UsuarioViewset, basename='Usuario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)

