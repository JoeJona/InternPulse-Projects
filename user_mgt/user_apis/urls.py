from django.urls import path
from . import views

urlpatterns = [
    path('users/all', views.get_all_user, name="get_all_user"),
    path('user/create', views.create_user, name="create_user"),
    path('user', views.user_by_name, name="get_user_by_name"),
    path('user/<uid>', views.user_by_id, name="get_user_by_id"),
]
