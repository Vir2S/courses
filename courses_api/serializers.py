from rest_framework import serializers
from courses_api.models import Course, Student, CourseParticipant


class CourseSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=250)
    # description = serializers.CharField(max_length=1000)
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()
    #
    # students = serializers.ManyRelatedField(Student, child_relation=None)
    #
    # def create(self, validated_data):
    #     return Course.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data('description', instance.description)
    #     instance.start_date = validated_data('start_date', instance.start_date)
    #     instance.end_date = validated_data('end_date', instance.end_date)
    #     instance.students = validated_data('students', instance.students)
    #     instance.save()
    #     return instance

    class Meta:
        model = Course
        fields = ['id', 'name', 'start_date', 'end_date', 'students']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']


class CourseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseParticipant
        fields = ['id', 'course']
