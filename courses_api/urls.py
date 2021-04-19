from django.urls import path
from courses_api.views import courses_list, course_detail, CoursesAPIView, CourseDetailsAPIView, CourseParticipantsAPIView, CourseParticipantDetailsAPIView

urlpatterns = [
    # path('courses/', courses_list),
    path('courses/', CoursesAPIView.as_view()),
    path('courseparticipants/', CourseParticipantsAPIView.as_view()),
    # path('course/<int:pk>/', course_detail),
    path('course/<int:id>/', CourseDetailsAPIView.as_view()),
    path('courseparticipant/<int:id>/', CourseParticipantDetailsAPIView.as_view()),
]
