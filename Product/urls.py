from django.urls import path, include

from .views import ProductDetailView,  RateProductView,submit_review





from . import views


urlpatterns = (
    # urls for Product
    path('', views.ProductListView.as_view(), name='Product_product_list'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='Product_product_detail'),
    
    path('rate-product/<int:product_id>/', RateProductView.as_view(), name='rate_product'),
     path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    
    

    

    # urls for order
    path('orders/', views.OrderListView.as_view(), name='Product_order_list'),
    path('order/conformed/', views.review_order_conformed, name='Product_order_conformed'),
    
    path('order/create/<slug:slug>', views.OrderCreateView.as_view(), name='Product_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(), name='Product_order_detail'),

    
    
    
    
    path('rate-product/<int:product_id>/', RateProductView.as_view(), name='rate_product'),  
     path('submit_review/<int:product_id>/', submit_review, name='submit_review'),

   
)



