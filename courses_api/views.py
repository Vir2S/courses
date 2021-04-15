from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from courses_api.models import Course, Student, CourseParticipant
from courses_api.serializers import CourseSerializer, StudentSerializer, CourseParticipantSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Generic API Views
class GenericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    # def post(self, request):
    #     return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# Class-Based Views
class CourseAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseParticipantsAPIView(APIView):

    def get(self, request):
        courses = CourseParticipant.objects.all()
        serializer = CourseParticipantSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseParticipantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseParticipantDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return CourseParticipant.objects.get(id=id)
        except CourseParticipant.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseParticipantSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = self.get_object(id)
        serializer = CourseParticipantSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Functional Views
@api_view(['GET', 'POST'])
def courses_list(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
