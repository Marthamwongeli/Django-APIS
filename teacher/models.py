from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    work_number = models.PositiveBigIntegerField()
    hire_date= models.DateField()
    office_hours=models.DurationField()
    faculty= models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    nationality=models.CharField(max_length=25)
    bank_account = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
