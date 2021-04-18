from django.urls import path
from courses_api.views import courses_list, course_detail, CourseAPIView, CourseDetailsAPIView, CourseParticipantsAPIView, CourseParticipantDetailsAPIView

urlpatterns = [
    # path('courses/', courses_list),
    path('courses/', CourseAPIView.as_view()),
    path('courseparticipants/', CourseParticipantsAPIView.as_view()),
    # path('course/<int:pk>/', course_detail),
    path('course/<int:id>/', CourseDetailsAPIView.as_view()),
    path('courseparticipant/<int:id>/', CourseParticipantDetailsAPIView.as_view()),
]
