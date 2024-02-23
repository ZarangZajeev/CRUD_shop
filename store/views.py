from django.shortcuts import render,redirect
from django.views.generic import View, CreateView,ListView,UpdateView,DeleteView,TemplateView
from store.forms import CategoryForm, ProductaddForm
from store.models import Category, Produuct
from django.urls import reverse


# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"

class CategoryView(CreateView):
    template_name="category_add.html"
    form_class=CategoryForm
    model=Category

    def get_success_url(self):
        return reverse("home")

class ProduuctAddView(CreateView):
    template_name="productadd.html"
    form_class=ProductaddForm
    model=Produuct

    def get_success_url(self):
        return reverse("home")


class ProductListView(ListView):
    template_name="Product_list.html"
    model=Produuct
    context_object_name="data"


class ProductUpdateView(UpdateView):
    template_name="product_edit.html"
    form_class=ProductaddForm
    model=Produuct

    def get_success_url(self):
        return reverse("home")
    
class ProductDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Produuct.objects.get(id=id).delete()
        return redirect("list")
    
class CategoryDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        category= Category.objects.get(id=id)
        product=Produuct.objects.filter(category_name=category)
        return render(request,"category_list.html",{"cat":product})