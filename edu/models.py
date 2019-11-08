from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    department = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    course_number = models.CharField(max_length=200)
    group_number = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    day= (('1','1'), ('2','2'), ('3','3'), ('4','4'))
    first_day = models.CharField(max_length=200,choices=day)
    second_day = models.CharField(max_length=200, choices=day)

