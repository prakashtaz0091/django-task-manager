from django.urls import path
from . import views
app_name = "day7"

urlpatterns = [
   path('', views.index, name='index'),
   path('accounts/login/', views.login_view, name='login_view'),
   path('logout_view/', views.logout_view, name='logout_view'),
   path('update_task/<int:task_id>/', views.update_task, name='update_task'),
   path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
   path('order_by_date/', views.order_by_date, name='order_by_date'),
   path('search/', views.search, name='search'),
]
