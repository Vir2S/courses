from django.http import HttpResponse
from courses_api.models import Course, Student
from django.db.models import Q
from courses_api.serializers import CoursesListSerializer, CourseDetailSerializer, StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import filters
# from rest_framework import generics, mixins
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny


# Class-Based Views
class CoursesAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        start_date = self.request.GET.getlist('start_date')
        end_date = self.request.GET.getlist('end_date')

        if start_date:
            courses = courses.filter(start_date__in=start_date)

        if end_date:
            courses = courses.filter(end_date__in=end_date)

        query = self.request.GET.get('q')

        if query:
            courses = courses.filter(Q(name__contains=query))

        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        try:
            course = self.get_object(id=id)
            serializer = CourseDetailSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        course = self.get_object(id)
        serializer = CourseDetailSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Functional Views
# @api_view(['GET', 'POST'])
# def courses_list(request):
#
#     if request.method == 'GET':
#         courses = Course.objects.all()
#         serializer = CoursesListSerializer(courses, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CoursesListSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def course_detail(request, pk):
#     try:
#         course = Course.objects.get(pk=pk)
#     except Course.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CourseDetailSerializer(course)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CourseDetailSerializer(course, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         course.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
