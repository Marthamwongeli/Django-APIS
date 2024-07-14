from django.urls import path, include
from .views      import StudentListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view')
]