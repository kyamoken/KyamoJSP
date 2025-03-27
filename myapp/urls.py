from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('update_page/', views.student_update_page, name='student_update_page'),
    path('delete_page/', views.student_delete_page, name='student_delete_page'),
]
