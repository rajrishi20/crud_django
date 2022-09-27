
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.employee_form,name='employee_insert'),#localhost:p/employee  
    #get and post req for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'),#get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'),#localhost:p/employee/list
    #get req. to retrive and display all records
]