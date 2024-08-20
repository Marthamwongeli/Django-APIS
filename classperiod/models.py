from django.db import models

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=100)
    course_level = models.CharField(max_length=2,blank=True, null=True)
    teacher = models.CharField(max_length=20, blank=True, null=True)
    classroom = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=2)
    semester = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.course} ({self.day_of_week})"

# Create your models here.
