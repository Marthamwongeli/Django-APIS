from django.db import models


class Courses(models.Model):
    course_name = models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    course_term = models.CharField(max_length=10)
    course_hours = models.PositiveSmallIntegerField()
    exam_method= models.CharField(max_length=20)
    course_department=models.CharField(max_length=20)
    course_description= models.TextField()
    course_instructor = models.CharField(max_length=20)
    course_fees=models.PositiveBigIntegerField()
    course_level = models.CharField(max_length=25)
    
    
    def __str__(self):
        return f"{self.course_name} {self.course_code}"





# Create your models here.
