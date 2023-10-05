from .models import Courses,Students
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        exclude = ['enrolled_student']

    def validate_course_code(self, value):
        # Your custom validation logic here
        if all(char.isalnum() or char.isspace() for char in value):
            return value
        raise serializers.ValidationError("Course code can only contain numbers, alphabets, and white spaces.")

class CourseSerializerEnrolled(serializers.ModelSerializer):
    class Meta:
        model = Courses  # Replace 'Course' with the actual model name for your courses
        fields = ['course_code', 'course_name']

class StudentSerializer(serializers.ModelSerializer):
    # enrolled=serializers.StringRelatedField(many=True, read_only=True)

    enrolled = serializers.SerializerMethodField()

    def get_enrolled(self, obj):
        #  enrolled is a related field to Course
        enrolled_courses = obj.enrolled.all()
        serialized_courses = CourseSerializerEnrolled(enrolled_courses, many=True).data
        return serialized_courses

    class Meta:
        model = Students
        fields = ['id', "first_name", "last_name", "s_id", "user_name", 'department','email', 'date_of_birth', 'gender','enrolled']

    def validate_s_id(self, value):
        # Custom validation logic for Student_id
        if value.isdigit():
            return value
        raise serializers.ValidationError("Student ID can only contain numbers.")
    
    def create(self, validated_data):
        # Extract the first_name and last_name from the validated data
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        # Generate a base user_name by concatenating first_name and last_name
        base_user_name = f"{first_name.lower()}.{last_name.lower()}"

        # Check if a user with the same user_name already exists
        user_name = base_user_name
        count = 1
        while Students.objects.filter(user_name=user_name).exists():
            user_name = f"{base_user_name}{count}"
            count += 1

        # Add the generated user_name to the validated data
        validated_data['department'] = user_name

        # Create and return the Student object with the updated user_name
        return Students.objects.create(**validated_data)