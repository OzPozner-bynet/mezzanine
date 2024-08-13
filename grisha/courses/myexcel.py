""" excel functions """

#my excel functions
#import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment
from .models import Student, Course, CourseCategory, StudentCourseMapping



def populate_course_sheet(worksheet, category):
    """ popluate the courses sheets 1 per category"""
    # Header row
    worksheet.cell(row=1, column=1, value="Student")
    column = 2
    for course in CourseCategory.filter(category=category):
        worksheet.cell(row=1, column=column, value=course.name)
        column += 1

    # Student data
    row = 2
    for student in Student.objects.all():
        worksheet.cell(row=row, column=1, value=student.display_name)
        column = 2
        for course in Course.objects.filter(category=category):
            mapping = StudentCourseMapping.objects.filter(student=student, course=course).first()
            if mapping:
                worksheet.cell(row=row, column=column, value=mapping.status)
            column += 1
        row += 1



def populate_dashboard_sheet(worksheet):
    """ fill the dashboard sheet"""
    # Header row
    worksheet.cell(row=1, column=1, value="Student")
    column = 2
    for category in CourseCategory.objects.all():
        worksheet.cell(row=1, column=column, value=category.name)
        column += 1

    # Student data
    row = 2
    for student in Student.objects.all():
        worksheet.cell(row=row, column=1, value=student.display_name)
        column = 2
        for category in CourseCategory.objects.all():
            completed_courses = StudentCourseMapping.objects.filter(
                student=student,
                course__category=category,
                status='completed'
            ).count()
            worksheet.cell(row=row, column=column, value=completed_courses)
            column += 1
        row += 1


def apply_conditional_formatting(worksheet):
    """ aplly cell format accourding to value"""
    # Assuming status values are 'completed', 'planned', and 'in_progress'
    green_fill = PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')
    yellow_fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    red_fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')


    for row in range(2, worksheet.max_row + 1):
        for col in range(2, worksheet.max_column + 1):
            cell = worksheet.cell(row=row, column=col)
            if cell.value == 'completed':
                cell.fill = green_fill
                cell.font = Font(name='Arial')
                cell.aligment = Alignment(horizontal='center')
            elif cell.value == 'planned':
                cell.fill = yellow_fill
            elif cell.value == 'in_progress':
                cell.fill = red_fill
