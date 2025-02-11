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
from django.urls import path
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
from logout.views import *

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', loading, name="loading"),
    path('welcome/', welcomepage, name='welcomepage'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('homepage/', homepage, name='homepage'),
    path('ebook/', ebook, name='ebook'),
    path('ebookpage1/', ebookpage1, name='ebookpage1'), 
    path('ebookpage2/', ebookpage2, name='ebookpage2'), 
    path('ebookpage3/', ebookpage3, name='ebookpage3'),
    path('ebookpage4/', ebookpage4, name='ebookpage4'),
    path('ebookpage5/', ebookpage5, name='ebookpage5'),
    path('audio/', audio, name='audio'),
    path('audiobook1/', audiobook1, name='audiobook1'),
    path('audiobook2/', audiobook2, name='audiobook2'),
    path('audiobook3/', audiobook3, name='audiobook3'),
    path('audiobook4/', audiobook4, name='audiobook4'),
    path('audiobook5/', audiobook5, name='audiobook5'),
    path('audiobookstore1/', audiobookstore1, name='audiobookstore1'),
    path('magazine/', magazine, name='magazine'),
    path('magazinebook1/', magazinebook1, name='magazinebook1'),
    path('magazinebook2/', magazinebook2, name='magazinebook2'),
    path('magazinebook3/', magazinebook3, name='magazinebook3'),
    path('magazinebook4/', magazinebook4, name='magazinebook4'),
    path('magazinebook5/', magazinebook5, name='magazinebook5'),
    path('album/', album, name='album'),
    path('albumstore2/', albumstore2, name='albumstore2'),
    path('albumstore3/', albumstore3, name='albumstore3'),
    path('albumstore4/', albumstore4, name='albumstore4'),
    path('albumstore5/', albumstore5, name='albumstore5'),
    path('albumstore6/', albumstore6, name='albumstore6'),
    path('albumstore7/', albumstore7, name='albumstore7'),
    path('albumstore8/', albumstore8, name='albumstore8'),
    path('audiobookstore/', audiobookstore, name='audiobookstore'),
    path('audiobookstore2/', audiobookstore2, name='audiobookstore2'),
    path('audiobookstore3/', audiobookstore3, name='audiobookstore3'),
    path('audiobookstore4/', audiobookstore4, name='audiobookstore4'),
    path('audiobookstore5/', audiobookstore5, name='audiobookstore5'),
    path('audiobookstore6/', audiobookstore6, name='audiobookstore6'),
    path('audiobookstore7/', audiobookstore7, name='audiobookstore7'),
    path('audiobookstore8/', audiobookstore8, name='audiobookstore8'),
    path('ebookstore/', ebookstore, name='ebookstore'),
    path('ebookstore1/', ebookstore1, name='ebookstore1'),
    path('ebookstore2/', ebookstore2, name='ebookstore2'),
    path('ebookstore3/', ebookstore3, name='ebookstore3'),
    path('ebookstore4/', ebookstore4, name='ebookstore4'),
    path('ebookstore5/', ebookstore5, name='ebookstore5'),
    path('ebookstore6/', ebookstore6, name='ebookstore6'),
    path('ebookstore7/', ebookstore7, name='ebookstore7'),
    path('ebookstore8/', ebookstore8, name='ebookstore8'),
    path('magazinestore/', magazinestore, name='magazinestore'),
    path('magazinestore1/', magazinestore1, name='magazinestore1'),
    path('magazinestore2/', magazinestore2, name='magazinestore2'),
    path('magazinestore3/', magazinestore3, name='magazinestore3'),
    path('magazinestore4/', magazinestore4, name='magazinestore4'),
    path('magazinestore5/', magazinestore5, name='magazinestore5'),
    path('magazinestore6/', magazinestore6, name='magazinestore6'),
    path('magazinestore7/', magazinestore7, name='magazinestore7'),
    path('magazinestore8/', magazinestore8, name='magazinestore8'),
    path('newpaper/', newpaper, name='newpaper'),
    path('payment/', payment, name='payment'),
    path('order/', order, name='order'),
]
