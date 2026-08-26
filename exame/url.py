from django.urls import path

from .views import (TeacherList,CourseCreate,LessonEdit,StudentDelete,EnrollmentDetail)

urlpatterns = [
    path("teachers/", TeacherList.as_view()),
    path("courses/create/", CourseCreate.as_view()),
    path("lessons/edit/<int:pk>", LessonEdit.as_view()),
    path("students/delete/<int:pk>", StudentDelete.as_view()),
    path("enrollments/<int:pk>/", EnrollmentDetail.as_view()),
]
