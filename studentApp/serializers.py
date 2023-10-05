from .models import Courses,Students
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

    def validate_course_code(self, value):
        # Your custom validation logic here
        if all(char.isalnum() or char.isspace() for char in value):
            return value
        raise serializers.ValidationError("Course code can only contain numbers, alphabets, and white spaces.")
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    # def validate_course_code(self, value):
    #     # Your custom validation logic here
    #     if any(char in "!@#$%^&*()[]{};:,.<>?/\\|~`" for char in value):
    #         raise serializers.ValidationError("Course code cannot contain special characters.")
    #     return value