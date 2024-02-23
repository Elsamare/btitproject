# vendor/urls.py
from django.urls import path
from .views import vendor_list, vendor_detail, vendor_create, vendor_update,user_login, user_logout, user_signup,vendor_delete

urlpatterns = [
    path('list/', vendor_list, name='vendor_list'),
    path('<int:pk>/', vendor_detail, name='vendor_detail'),
    path('create/', vendor_create, name='vendor_create'),
    path('<int:pk>/update/', vendor_update, name='vendor_update'),
    path('<int:pk>/delete/', vendor_delete, name='vendor_delete'),

    path('create/', vendor_create, name='vendor_create'),
    

    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/', user_signup, name='user_signup'),
]
