from django.urls import path, include
from .views import *

urlpatterns = [
    path('student/details', StudentDetails.as_view()), # api route to get perticular student details
    path('teacher/update/subjects', UpdateSubjects.as_view()), # api route to update subjects for perticular teacher
    path('students/report', StudentsReport.as_view())   #  route to report of all students

]
