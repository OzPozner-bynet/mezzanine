from django.urls import path
from . import views

urlpatterns = [
    path('', views.solution_list, name='solution_list'),
    path('he/solutions/', views.solution_list, name='solution_list'),
    path('solutions/', views.solution_list, name='solution_list'),
    path('solutions/<slug:slug>/', views.solution_detail, name='solution_detail'),
    path('he/solutions/<slug:slug>/', views.solution_detail, name='solution_detail'),
   # path('solutions/<slug:slug>/', views.solution_detail, name='solution_detail'),
]