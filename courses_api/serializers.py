from rest_framework import serializers
from .models import Course, Student, CourseParticipant


class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=1000)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        return Course.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data('description', instance.description)
        instance.start_date = validated_data('start_date', instance.start_date)
        instance.end_date = validated_data('end_date', instance.end_date)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']


class CourseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'students_count']