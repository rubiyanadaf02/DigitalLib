"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from loading.views import *
from welcomepage.views import *
from login.views import *
from signup.views import *
from homepage.views import *
from ebook.views import *
from audio.views import *
from magazine.views import *
from album.views import *
from newpaper.views import *

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', loading, name="loading"),
    path('welcome/', welcomepage, name='welcomepage'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('homepage/', homepage, name='homepage'),
    path('ebook/', ebook, name='ebook'),
    path('ebookpage1/',ebookpage1, name='ebookpage1'), 
    path('ebookpage2/',ebookpage2, name='ebookpage2'), 
    path('ebookpage3/',ebookpage3, name='ebookpage3'),
    path('ebookpage4/',ebookpage4, name='ebookpage4'),
    path('ebookpage5/',ebookpage5, name='ebookpage5'),
    path('audio/',audio, name='audio'),
    path('audiobook1/',audiobook1, name='audiobook1'),
    path('audiobook2/',audiobook2, name='audiobook2'),
    path('audiobook3/',audiobook3, name='audiobook3'),
    path('audiobook4/',audiobook4, name='audiobook4'),
    path('audiobook5/',audiobook5, name='audiobook5'),
    path('magazine/',magazine, name='magazine'),
    path('magazinebook1/',magazinebook1, name='magazinebook1'),
    path('magazinebook2/',magazinebook2, name='magazinebook2'),
    path('magazinebook3/',magazinebook3, name='magazinebook3'),
    path('magazinebook4/',magazinebook4, name='magazinebook4'),
    path('magazinebook5/',magazinebook5, name='magazinebook5'),
    path('album/',album, name='album'),
    path('audiobookstore/',audiobookstore, name='audiobookstore'),
    path('ebookstore/',ebookstore, name='ebookstore'),
    path(' magazinestore/', magazinestore, name='magazinestore'),
    path('newpaper/',newpaper, name='newpaper'),
    path('payment/',payment, name='payment'),
    path('order/',order, name='order'),

]