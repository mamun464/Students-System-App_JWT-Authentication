"""
URL configuration for studentApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentApp import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Course api url
    path('api/students',views.StudentsViews.as_view(), name="students-details"),
    path('api/students/update/<int:pk>',views.StudentsViews.as_view(), name="students-updated"),
    path('api/students/<int:pk>',views.singleStudentView.as_view(), name="student-list"),
    path('api/students/delete/<int:pk>',views.StudentsViews.as_view(), name="students-Deleted"),

    # Course api url
    path('api/courses/',views.CourseViews.as_view(), name="courses-details"),
    path('api/courses/update/<int:pk>',views.CourseViews.as_view(), name="courses-updated"),
    path('api/courses/<int:pk>',views.singleCourseView.as_view(), name="courses-list"),
    path('api/courses/delete/<int:pk>',views.CourseViews.as_view(), name="courses-Deleted"),

    #JWT access token
    path('api/gettoken',TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path('api/refreshtoken',TokenRefreshView.as_view(), name="token-Refresh"),
    path('api/verifytoken',TokenVerifyView.as_view(), name="token-verify"),
]


