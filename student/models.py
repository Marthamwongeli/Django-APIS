from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length=28)
    code = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=27)
    Student_class = models.CharField(max_length=20)
    Student_picture = models.ImageField()
   
   
    

    def _str_(self):
       return f"{self.first_name} {self.last_name}"