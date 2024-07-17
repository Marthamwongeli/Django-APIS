from django.db import models


from django.db import models
from teacher.models import Teacher

class Courses(models.Model):
    course_id =models.IntegerField()
    course_name =models.CharField(max_length = 20)
    teacher_code= models.ForeignKey(Teacher,default=1,  on_delete=models.CASCADE, related_name= 'teacher_code')
    topics = models.TextField()
    course_room= models.CharField(max_length=20)
    
    
    
    def __str__(self):
          return f"{self.course_name} {self.course_id}"

# Create your models here.
