import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from courses_api.serializers import CoursesListSerializer, CourseDetailSerializer
from courses_api.models import Course


class CourseTestCase(APITestCase):
    list_url = reverse('courses-list')

    def setUp(self):
        self.name = 'test course'
        self.description = 'test course description'
        self.start_date = '2021-04-24'
        self.end_date = '2021-05-05'
        self.lectures = 10
        self.students = [
            6
        ]

    def test_get_courses_list(self):
        response = self.client.get(self.list_url)
        no_response = self.client.get('/api/courses-courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(no_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_course(self):
        data = {
            'name': 'test name',
            'description': 'test description',
            'start_date': '2021-04-24',
            'end_date': '2021-05-05',
            'lectures': '5',
            'students': []
        }
        response = self.client.post('/api/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_course_detail(self):
        response = self.client.get(reverse('course-detail', kwargs={'pk': 1}))
        no_response = self.client.get(reverse('course-detail', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(no_response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_update_course(self):
    #     data = {
    #         'name': 'test name',
    #         'description': 'test description',
    #         'start_date': '2021-04-24',
    #         'end_date': '2021-05-05',
    #         'lectures': '5',
    #         'students': []
    #     }
    #     response = self.client.put(reverse('course-detail', kwargs={'pk': 1}), data)
    #     self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    # def test_delete_course(self):
    #     response = self.client.delete()
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
