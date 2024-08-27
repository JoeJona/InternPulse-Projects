from django.urls import path
from . import views

urlpatterns = [
    path('employees/all', views.get_all_employee, name="get_all_user"),
    path('employee/create', views.create_employee, name="create_employee"),
    path('employee/<eid>', views.employee_by_id, name="employee_by_id"),
    path('employee/deactivate/<eid>', views.deactivate_employee, name="deactivate_employee"),
    path('employees/active-employees', views.all_active_employees, name="all_active_employees"),
    path('give-review', views.give_review_employee, name="give_review_employee"),
]
