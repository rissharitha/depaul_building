"""BuildConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from Build import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.register),
    path('registerbuttonclick',views.registerbuttonclick),
    path('view_and_edit_profile',views.view_and_edit_profile),
    path('view_and_edit_profilebuttonclick',views.view_and_edit_profilebuttonclick),
    path('update/<id>', views.update),
    path('update_post/<id>',views.update_post),
    path('delete/<id>', views.delete),
    path('add_portfolio',views.add_portfolio),
    path('add_portfoliobuttonclick',views.add_portfoliobuttonclick),
    path('edit_portfolio',views.edit_portfolio),
    path('edit_portfoliobuttonclick/<id>',views.edit_portfoliobuttonclick),
    path('view_portfolio',views.view_portfolio),
    path('view_user_request',views.view_user_request),
    path('approve/<id>',views.approve),
    path('reject/<id>',views.reject),
    path('approve_request',views.approve_request),
    path('add_budget/<id>',views.add_budget),
    path('add_budgetbuttonclick/<id>',views.add_budgetbuttonclick),
    path('view_status',views.view_status),
    path('add_material/<id>',views.add_material),
    path('view_material/<id>',views.view_material),
    path('delete_material/<id>',views.delete_material),
    path('add_materialtbuttonclick/<id>',views.add_materialtbuttonclick),
    path('add_advance_amount',views.add_advance_amount),
    path('add_advance_amountbuttonclick',views.add_advance_amountbuttonclick),
    path('view_advance_amount/<id>',views.view_advance_amount),
    # path('view_full_payment',views.view_full_payment),
    path('view_complaint_from_user',views.view_complaint_from_user),
    path('send_reply/<id>',views.send_reply),
    path('send_replybuttonclick/<id>',views.send_replybuttonclick),
    path('change_password',views.change_password),
    path('change_passwordbuttonclick', views.change_passwordbuttonclick),
    path('view_review_and_rating',views.view_review_and_rating),
    path('',views.index),
    path('loginS',views.loginS),
    path('loginbuttonclick',views.loginbuttonclick),
    path('workerlink',views.workerlink),

]
