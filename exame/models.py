from django.db import models

# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    vidio_url = models.URLField()
    duration = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
