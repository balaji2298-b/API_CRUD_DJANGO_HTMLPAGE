from django.urls import path
from myapp import views 

urlpatterns = [
    path('',views.ApiOverview, name='home'),
    path('insert/', views.add_items, name='add_items'),
    path('display/', views.view_items, name='view_items'),
    path('page/update/<str:mobilenumber>', views.update_items, name='update_items'),
    path('page/delete/<int:pk>', views.delete_items, name='delete_items'),
   
]