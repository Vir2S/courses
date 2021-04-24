from django.urls import path
# from courses_api.views import courses_list, course_detail
from courses_api.views import CoursesAPIView, CourseDetailAPIView

urlpatterns = [
    # path('courses/', courses_list),
    path('api/courses/', CoursesAPIView.as_view(), name='courses-list'),
    # path('course/<int:pk>/', course_detail),
    path('api/course/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
]
