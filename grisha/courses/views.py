""" controll app views """
#import csv
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from myexcel import populate_dashboard_sheet, populate_course_sheet, populate_student_sheet 
from .models import Student, Course, CourseCategory
from .forms import StudentForm, CourseForm

def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    context = {'students': students, 'courses': courses}
    return render(request, 'students_courses/index.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students_courses/student_form.html', {'form': form})

# Similar views for add_course, edit_student, edit_course, delete_student, delete_course

def import_excel(request):
    """ implement import"""
    print("TODO") # ... Excel import logic using openpyxl or similar library


def export_excel(request):
    """ implement export"""
    import openpyxl
    from openpyxl.styles import PatternFill, Font, Alignment
    """
    Exports data to an Excel file.

    Args:
        data: A dictionary containing data to be exported.
            Structure: {
                'sheet1_data': [list of data for sheet 1],
                'sheet2_data': [list of data for sheet 2],
                ...
            }

    Returns:
        The path to the exported Excel file.
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.create_sheet("Dashboard")
    populate_dashboard_sheet(worksheet)
    worksheet = workbook.create_sheet("students")
    populate_student_sheet(worksheet)
    # Create worksheets and populate data
    for my_cat in CourseCategory:
        worksheet = workbook.create_sheet(my_cat)
        populate_course_sheet(worksheet, my_cat)
        # Populate worksheet with sheet_data

    # Apply conditional formatting (example)
    #for row in sheet1['A2:A10']:
    #    for cell in row:
    #        if cell.value > 10:
    #            cell.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    

    # Save the workbook
    file_path = 'exported_data.xlsx'
    workbook.save(file_path)
    return file_path
    print("TODO")
    # ... Excel export logic using openpyxl or similar library
