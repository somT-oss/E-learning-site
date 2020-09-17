from django.db import models
from django.contrib.auth.models import User 

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_author = models.ForeignKey(User, on_delete=models.CASCADE)
    course_image = models.ImageField(upload_to='course_profile_pics', null=True)
    course_datestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.course_name} was created on {self.course_datestamp}"

class CourseOutline(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_description = models.TextField()

    def __str__(self):
        return f"Course for {self.course_name}"


# Create your models here.
