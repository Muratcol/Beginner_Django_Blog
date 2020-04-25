"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from article import views
from article.models import Article
from django.conf import settings
from django.conf.urls.static import static
app_name = "article"


urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addarticle, name = "add_article"),
    path("<int:id>/" , views.article, name = "article"),
    path('delete/<int:id>/', views.deletearticle, name = "delete"),
    path('update/<int:id>/', views.updatearticle, name = "update"),
    path('', views.article_show, name = "article_show"),
    path('comment/<int:id>/', views.addcomment, name = "comment"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
