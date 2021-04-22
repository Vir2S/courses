from rest_framework import serializers
from courses_api.models import Course, Student, CourseParticipant


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'students']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']


class CourseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseParticipant
        fields = ['id', 'course', 'student']
