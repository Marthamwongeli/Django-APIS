from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
class StudentListView(APIView):
    def get(self,  request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
# Create your views here.
