from django.shortcuts import render
from rest_framework import generics
from course.models import Courses
from .serializers import CoursesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
# from course.models import Courses
# from .serializers import CoursesSerializer
# # api/views.py

# from .serializers import CoursesSerializer

class StudentListView(APIView):
    def get(self, request):
        Students = Student.object.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request):
        Teachers = Teacher.object.all()
        serializer = TeacherSerializer(Teachers, one=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriods = ClassPeriod.cbject.all()
        serializer = ClassPeriodSerializer(ClassPeriods, many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self, request):
        course = CoursesSerializer.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)
    
class ClassListView(APIView):
    def get(self, request):
        course = Courses.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)
    
class CourseListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer








