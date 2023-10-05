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



class CourseViews(APIView):
    #Get Course Info
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
    

