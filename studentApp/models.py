from django.db import models


#student Model or database
class Students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    s_id=models.CharField(max_length=50,unique=True)
    user_name=models.CharField(max_length=100,unique=True,null=True)
    department=models.CharField(max_length=100)
    email=models.EmailField()
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Students"
    

    def __str__(self):
        return f' {self.first_name} ({self.s_id})'


#course Model
class Courses(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    #enrolled_student=models.ForeignKey(Students, on_delete=models.CASCADE,related_name="student", null=True)
    enrolled_student = models.ManyToManyField(Students, related_name="enrolled", null=True)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return f' {self.course_name} ({self.course_code})'



