from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import CoursesDetailView
from .views import ClassPeriodDetailView
from .views import TeacherDetailView


urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view'),
    path("teachers/", TeacherListView.as_view(),name="teacher_list_view"),
    path("courses/", CourseListView.as_view(),name="course_list_view"),
    path("classPeriod/",ClassPeriodListView.as_view(),name="class_Period_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name="student_detailview"),
    path("courses/<int:id>/",CoursesDetailView.as_view(),name="course_list_view" ),
    path("classPeriod/<int:id>/",ClassPeriodDetailView.as_view(),name="class_Period_detailview"),
    path("teachers/<int:id>/",TeacherDetailView.as_view(),name="teacher_detailview")
]