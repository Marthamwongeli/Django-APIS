# from rest_framework import serializers
# from student.models import Student
# from teacher.models import Teacher
# from course.models import Courses
# from classperiod.models import ClassPeriod
       
from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Courses
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"
        
class CoursesSerializer(serializers.ModelSerializer):  # Corrected class name
    class Meta:
        model = Courses
        fields = "__all__"
