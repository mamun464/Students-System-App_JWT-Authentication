from django.shortcuts import render
from .serializers import CourseSerializer,StudentSerializer
from .models import Students,Courses
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentsViews(APIView):
    def get(self,request):
        students=Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass

#single course view
class singleCourseView(APIView):

    def get(self, request, pk):
        try:
             course=Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    

#single Student view
class singleStudentView(APIView):

    def get(self, request, pk):
        try:
             student_single=Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student_single)
        
        return Response(serializer.data,status=status.HTTP_200_OK)

class CourseViews(APIView):
    #Get all Course Info
    def get(self,request):
        course=Courses.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    
    #create Course
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Updating Course
    def put(self,request,pk):

        try:
            course=Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=CourseSerializer(course,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #for deleted course
    def delete(self, request, pk):
        try:
             course=Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#for student Information View
class StudentsViews(APIView):
    #Get All students Info
    def get(self,request):
        students=Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    


     #create Student
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


     #Updating Student
    def put(self,request,pk):

        try:
            student_update=Students.objects.get(pk=pk)
        except Students.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializer(student_update,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    #for deleted Student
    def delete(self, request, pk):
        try:
             delete_student=Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        delete_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

