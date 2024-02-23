from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order,ReviewRating
from .forms import OrderForm,ReviewForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from django.views import View




class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
     model = Product
     template_name = 'Product/product_detail.html'


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    average_rating = product.average_rating()

    return render(request, 'product_detail.html', {'product': product, 'average_rating': average_rating})
     
def submit_review(request, product_id):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            review=ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form=ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, 'thank you it has been updated')
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.rating=form.cleaned_data['rating']
                data.review=form.cleaned_data['review']
                data.ip=request.META.get('REMOTE_ADDR')
                data.product_id=product_id
                data.user = request.user
                data.save()
                messages.success(request, 'thank you it has been submitted')
                return redirect(url)




@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/conformed/'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        messages.success(self.request, 'Thank you! It has been submitted')
        
        return context
    

    
    

    
        


    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug__iexact=slug)
        form.instance.product = product
        form.instance.cost = int(form.instance.count) * int(product.price)
        return super(OrderCreateView, self).form_valid(form)
    


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order




def review_order_conformed(request):
    
    return render(request, 'Product/thanks.html')





class RateProductView(View):
    template_name = 'Product/rate_product.html'  # Create a template for the rating form

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, self.template_name, {'product': product})
