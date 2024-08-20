"""django admin registration """


from django.contrib import admin
from .models import Student, Course, CourseCategory, StudentCourseMapping

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(StudentCourseMapping)
