from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    teacher_id = models.IntegerField(primary_key=True)
    teacher_image = models.ImageField()
    
    
    def _str_(self):
       return f"{self.first_name} {self.last_name}"
     