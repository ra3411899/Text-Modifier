# from cgitb import text
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls), # Admin Controls
    path('', views.index, name = 'index'), # Home Page
    # path('home/', views.index, name = 'index'), # Home Page
    path('about/', views.about_us, name = 'about'), # About Page
    path('analyze/', views.analyze_text, name = "analyze_Text_Editor"), # Button Action 
]
