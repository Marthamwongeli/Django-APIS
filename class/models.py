from django.db import models


class Classes (models.Model):
    class_name = models.CharField(max_length=20)
    class_id = models.PositiveSmallIntegerField()
    class_course = models.CharField(max_length=20)
    class_trainer = models.CharField(max_length=20)
    class_days= models.PositiveSmallIntegerField()
    academic_year=models.CharField(max_length=20)
    class_capacity= models.PositiveSmallIntegerField()
    class_enrollment = models.PositiveBigIntegerField()
    room_number=models.PositiveSmallIntegerField()
    class_windows = models.PositiveSmallIntegerField()
def __str__(self):
    return f"{self.class_name} {self.class_id}"

# Create your models here.
