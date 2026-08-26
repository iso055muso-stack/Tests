from django.shortcuts import render
from.serializers import TeacherSerializer,LessonSerializer,StudentSerializer,EnrollmentSerializer,CourseSerializer
from rest_framework import generics
from .models import Teacher,Student,Course,Lesson,Enrollment
# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonEdit(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentDelete(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentDetail(generics.RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer