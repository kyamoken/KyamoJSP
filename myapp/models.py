from django.db import models

class Student(models.Model):
    student_number = models.IntegerField()
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name