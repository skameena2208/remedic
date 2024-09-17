"""
URL configuration for customer project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from customerapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('customer',views.customer,name="customer"),
    path('register',views.register,name="register"),
    path('customer_home',views.customer_home,name="customer_home"),
    path('logout',views.logout,name="logout"),
    path('customer_profile',views.customer_profile,name="customer_profile"),
    path('admin',views.admin,name="admin"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('logout1',views.logout1,name="logout1"),
    path('view_contact',views.view_contact,name="view_contact"),
    path('view_customer', views.view_customer, name="view_customer"),
    path('accept_customer/<int:id>',views.accept_customer,name="accept_customer"),
    path('reject_customer/<int:id>', views.reject_customer, name="reject_customer"),
    path('edit',views.edit,name="edit"),
    path('update',views.update,name="update"),
    path('deActive_customer/<int:id>',views.deActive_customer,name="deActive_customer"),
    path('customer_change_password',views.customer_change_password,name="customer_change_password"),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)