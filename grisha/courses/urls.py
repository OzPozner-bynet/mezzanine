""" Register app urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/students_courses/', views.index, name='index'),
    path('add_student/', views.add_student, name='add_student'),
    #path('courses/', views.courses, name='courses'),
    # ... other URL patterns
    path('import_excel/', views.import_excel, name='import_excel'),
    path('export_excel/', views.export_excel, name='export_excel'),
]
