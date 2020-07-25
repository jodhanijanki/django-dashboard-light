# -*- encoding: utf-8 -*-


from django.urls import path
from .views import login_view, register_user,productview, bankdetails,analyse, companyuser,indivisualuser,statement
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("indivisualuser/", indivisualuser, name="indivisualuser"),
    path("companyuser", companyuser, name="companyuser"),
    path('bankdetails',bankdetails,name='bankdetails'),
    path('statement',statement,name='statement'),
    path('productview',productview,name='productview'),
    path('analyse',analyse,name='analyse')

]
