""" controll app views """

#import csv
import openpyxl
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.http import FileResponse

from .myexcel import autofit_column_widths, populate_dashboard_sheet, populate_course_sheet
from .myexcel import populate_student_sheet, sanitize_sheet_name,apply_conditional_formatting
from .models import Student, Course, CourseCategory
from .forms import StudentForm #, CourseForm
#from django.conf import settings

def courses(request):
    """ handle courses view"""
    mystudents = Student.objects.all()
    mycourses = Course.objects.all()
    context = {'students': mystudents, 'courses': mycourses}
    return render(request, 'students_courses/index.html', context)


def index(request):
    """ handel main index"""
    mystudents = Student.objects.all()
    mycourses = Course.objects.all()
    context = {'students': mystudents, 'courses': mycourses}
    return render(request, 'students_courses/index.html', context)

def add_student(request):
    """ should handeling adding students corrently in Admin so it is NOT implemented here"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students_courses/student_form.html', {'form': form})

# Similar views for add_course, edit_student, edit_course, delete_student, delete_course

def delete_sheet_if_exists(workbook, sheet_name):
    """Deletes a sheet if it exists in the workbook.

    Args:
      workbook: The openpyxl workbook object.
      sheet_name: The name of the sheet to delete.
    """

    if sheet_name in workbook.sheetnames:
        workbook.remove(workbook[sheet_name])


def import_excel(request):
    """ implement import"""
    print("TODO") # ... Excel import logic using openpyxl or similar library
    form = ""
    return render(request, 'students_courses/import_excel.html', {'form': form})


def export_excel(request):
    """ implement export
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
    if request:
        print(str(request))
    workbook = openpyxl.Workbook()
    worksheet = workbook.create_sheet("Dashboard")
    populate_dashboard_sheet(worksheet)
    autofit_column_widths(worksheet)
    worksheet = workbook.create_sheet("students")
    populate_student_sheet(worksheet)
    autofit_column_widths(worksheet)
    # Create worksheets and populate data
    for my_cat in CourseCategory.objects.all():
        sheet_name = sanitize_sheet_name(str(my_cat))
        worksheet = workbook.create_sheet(sheet_name)
        populate_course_sheet(worksheet, str(my_cat))
        apply_conditional_formatting(worksheet)
        autofit_column_widths(worksheet)

    file_path = 'exported_data.xlsx'
    delete_sheet_if_exists(workbook,"Sheet")
    workbook.save(file_path)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="students_courses.xlsx"'
    return response
