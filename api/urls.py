from django.urls import path
from .views import StudentListViews
from .views import TeacherListViews
from .views import CoursesListViews
from .views import ClassPeriodListViews
from .views import StudentDetailView
from .views import CoursesDetailView
from .views import ClassPeriodDetailView
from .views import TeacherDetailView


urlpatterns = [
    path('student/', StudentListViews.as_view(), name = 'student_list_view'),
    path("teachers/", TeacherListViews.as_view(),name="teacher_list_view"),
    path("courses/", CoursesListViews.as_view(),name="course_list_view"),
    path("classPeriod/",ClassPeriodListViews.as_view(),name="class_Period_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name="student_detailview"),
    path("courses/<int:id>/",CoursesDetailView.as_view(),name="course_list_view" ),
    path("classPeriod/<int:id>/",ClassPeriodDetailView.as_view(),name="class_Period_detailview"),
    path("teachers/<int:id>/",TeacherDetailView.as_view(),name="teacher_detailview")
]