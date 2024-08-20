# course/models.py
from django.db import models
from django.contrib.auth.models import User
from mezzanine.core.fields import RichTextField


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return(f"{self.display_name}")

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager()
    # Example: If you want to display "name (id)"
    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    description = RichTextField()  # For detailed course information
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} ({self.category})"

class StudentCourseMapping(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'),
                                                      ('planned', 'Planned'),
                                                      ('in_progress', 'In Progress')])
    completion_date = models.DateField(null=True, blank=True)
    objects = models.Manager()
