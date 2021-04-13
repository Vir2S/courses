from django.urls import path
from courses_api.views import courses_list, course_detail

urlpatterns = [
    path('courses/', courses_list),
    path('course/<int:pk>/', course_detail),
]
