from django.urls import path
from courses_api.views import courses_list, course_detail, CourseAPIView, CourseDetailsAPIView, GenericAPIView

urlpatterns = [
    # path('courses/', courses_list),
    path('courses/', CourseAPIView.as_view()),
    # path('course/<int:pk>/', course_detail),
    path('course/<int:id>/', CourseDetailsAPIView.as_view()),
    path('generic/course/<int:id>/', GenericAPIView.as_view()),
]
