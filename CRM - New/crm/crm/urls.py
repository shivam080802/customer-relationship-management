"""
URL configuration for crm project.

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
from django.contrib import admin
from django.urls import path, include
from lead import views
from lead.views import LeadRetrieve, CompanyRetrieve, UserRetrieve, CreateUser, GetUser, Count
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'',views.LeadViewset)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('get-lead/',views.CreateLead.as_view()),
    # path('generate_random_companies/', GenerateRandomCompanies.as_view(), name='generate_random_companies'),
    path('le/<int:pk>',LeadRetrieve.as_view()),
    path('delete-lead/<int:pk>',views.DeleteLead.as_view()),
    path('update-lead/<int:pk>',views.UpdateLead.as_view()),
    path('company/',views.GetCompany.as_view()),
    path('company/<int:pk>',CompanyRetrieve.as_view()),
    path('user/<int:pk>',UserRetrieve.as_view()),
    path('postuser/',CreateUser.as_view()),
    path('user/',GetUser.as_view()),
    path('count/',Count.as_view()),
]