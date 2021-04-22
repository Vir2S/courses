from rest_framework import serializers
from courses_api.models import Course, Student


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'lectures', 'students']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']
