from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),#get and post req. for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'),#get and post req. for update operation
    path('delete<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),#get and post req. for display all records
    path('home/', views.home,name = 'home'),
    path('homepage/', views.home,name = 'homepage'),
    path('About/', views.About,name = 'About'),
    path('Login_form/', views.Login_form,name = 'Login_form'),
    path('login/', views.login,name = 'login'),
     path('logout/', views.logout,name = 'logout'),

]