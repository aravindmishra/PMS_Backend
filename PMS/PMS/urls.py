"""PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from medicine import views as medicineView 
from bill import views as billView 
from user import views as userView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicine/add', medicineView.AddMedicine.as_view()),
    path('medicine/update/<id>', medicineView.UpdateMedicine.as_view()),
    path('medicine/list', medicineView.MedicineList.as_view()),
    path('customer/check', billView.CheckCustomer.as_view()),
    path('bill/add', billView.BillEntry.as_view()),
    path('bill/list', billView.BillDetailsList.as_view()),
    path('purchase/list', billView.PurchaseDetailsList.as_view()),
    path('purchase/filter', billView.FilterPurchaseDetails.as_view()),
    path('user/add', userView.AddUser.as_view()),
    path('user/update/<id>', userView.UpdateUser.as_view()),
    path('user/list', userView.UserDetailsList.as_view()),
    path('user/check', userView.CheckUserAuth.as_view()),
]
