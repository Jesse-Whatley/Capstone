from typing import Any
from django.views.generic import DetailView, ListView
from .models import Category, Product
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from .forms import OrderForm
# Create your views here.

def set_liked_by_user(products, user):
    if not isinstance(products, list):
        products = [products]
        
    for product in products:
        if user.is_authenticated:
            product.liked = user in product.liked_by.all()
        else:
            product.liked = False
    return products

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.kwargs.get('category', None)
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(context['object_list'])
        context['object_list'] = products
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class LikeProductView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        
        if request.user in product.liked_by.all():
            product.liked_by.remove(request.user)
        else:
            product.liked_by.add(request.user)
        
        referer_url = request.META.get('HTTP_REFER', reverse('product_list'))
        return_url = reverse('product_detail', args=[product_id])
        if return_url not in referer_url:
            return_url = reverse('product_list')
        
        return HttpResponseRedirect(return_url)
    
    
    

def order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            street = form.cleaned_data["street"]
            street_2 = form.cleaned_data["street_2"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zip_code = form.cleaned_data["zip_code"]
            delivery_instructions = form.cleaned_data["delivery_instructions"]
            
            
            
            # Save a new Order record using Order model
            
            # Call PayPal API
            
            
            return redirect('order_details')
        
        else:
            print("invalid form")
    else:
        form = OrderForm()
    return render(request, 'store/order_details.html', {'form': form})