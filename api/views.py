from django.shortcuts import render

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
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
class TeacherListView(APIView):
    def get(self, request):
        Teachers = Teacher.object.all()
        serializer = TeacherSerializer(Teachers, one=True)
        return Response(serializer.data)
    
    
    
    def post(self,request):
        serializer= TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriods = ClassPeriod.cbject.all()
        serializer = ClassPeriodSerializer(ClassPeriods, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer= ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
    
class CourseListView(APIView):
    def get(self, request):
        course = CoursesSerializer.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer= CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        

    
class StudentDetailView(APIView):
    def get(self,request,id):
        Students = Student.objects.get(id=id)
        serializer = StudentSerializer(Students)
        return Response(serializer.data)
    
    
    
    def put(self,request,id):
        student= Student.objects.get(id=id)
        serializer= StudentSerializer(student,data=request.data)
        if serializer.is_valid():
          serializer.save
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
class TeacherDetailView(APIView):
    def get(self,request,id):
        Teachers = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(Teachers)
        return Response(serializer.data)
    
    
    
    def put(self,request,id):
        Teacher= Teacher.objects.get(id=id)
        serializer= TeacherSerializer(Teacher,data=request.data)
        if serializer.is_valid():
          serializer.save
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,id):
        Teacher = Teacher.objects.get(id=id)
        Teacher.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    


class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(ClassPeriod)
        return Response(serializer.data)
    
    
    
    def put(self,request,id):
        ClassPeriod= ClassPeriod.objects.get(id=id)
        serializer= ClassPeriodSerializer(ClassPeriod,data=request.data)
        if serializer.is_valid():
          serializer.save
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        ClassPeriod.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
   
        
class CoursesDetailView(APIView):
    def get(self,request,id):
        Courses = Courses.objects.get(id=id)
        serializer = CoursesSerializer(Courses)
        return Response(serializer.data)
    
    
    
    def put(self,request,id):
        Courses= Courses.objects.get(id=id)
        serializer= CoursesSerializer(Courses,data=request.data)
        if serializer.is_valid():
          serializer.save
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,id):
        Courses = Courses.objects.get(id=id)
        Courses.delete()
        return Response(status= status.HTTP_202_ACCEPTED)








