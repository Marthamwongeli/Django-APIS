from django.urls import path, include
from .views import StudentListView
from .views import StudentDetailView

urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view'),
    path('student/<int:id>/',StudentDetailView.as_view(),name= 'StudentDetailView')
]