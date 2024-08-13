# course/models.py
from django.db import models
from django.contrib.auth.models import User
from mezzanine.core.fields import RichTextField


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)

class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    description = RichTextField()  # For detailed course information

class StudentCourseMapping(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'),
                                                      ('planned', 'Planned'),
                                                      ('in_progress', 'In Progress')])
    completion_date = models.DateField(null=True, blank=True)
