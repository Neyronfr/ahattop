"""
URL configuration for news_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from news_site import views
from news_site.views import HomePage, search_results, article_page, category_page,MyLoginView, logout_view, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name='home'),
    path('search_results', search_results),
    path('articles/<int:pk>', article_page),
    path('category/<int:pk>', category_page),
    path("<int:pk>/article", views.NewsDetailView.as_view(), name='article'),
    path("create/", views.NewsCreateView.as_view(), name='create'),
    path("edit/<int:pk>", views.NewsUpdateView.as_view(), name='edit'),
    path("delete/<int:pk>", views.NewsDeleteView.as_view(), name='delete'),
    path('login/', MyLoginView.as_view()),
    path('logout/', logout_view),
    path("contact/", contact_us, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
