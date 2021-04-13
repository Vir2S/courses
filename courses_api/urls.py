from django.urls import path
from courses_api.views import courses_list

urlpatterns = [
    path('courses/', courses_list),
]
