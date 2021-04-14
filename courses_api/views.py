from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from courses_api.models import Course, Student
from courses_api.serializers import CourseSerializer, StudentSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def courses_list(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = CourseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=204)
