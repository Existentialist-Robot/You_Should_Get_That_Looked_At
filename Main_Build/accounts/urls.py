from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='Signup'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    # path('email_signup/', views.email_signup_view, name='Email')

]
