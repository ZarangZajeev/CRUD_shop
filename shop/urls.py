"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.IndexView.as_view(),name="home"),
    path("product/add",views.ProduuctAddView.as_view(),name="product_add"),
    path("category/add",views.CategoryView.as_view(),name="category"),
    path("product/list",views.ProductListView.as_view(),name="list"),
    path("product/<int:pk>/change",views.ProductUpdateView.as_view(),name="change"),
    path("product/<int:pk>/remove",views.ProductDeleteView.as_view(),name="remove"),
    path("category/<int:pk>/list",views.CategoryDetailView.as_view(),name="cat-list"),
]
