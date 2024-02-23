# accounts/urls.py
''''from django.urls import path

from django.contrib.auth import views as auth_views
from .views import SignUp


from django import views
urlpatterns = [
    
     path('signup/', SignUp.as_view(), name='signup'),
     
    

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]'''

from django.contrib.auth import views as auth_views

# accounts/urls.py
from django.urls import path
from .views import signup,  user_logout,user_login
urlpatterns = [
 path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]


