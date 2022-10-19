from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import *
from .models import *
from .serializers import *



# Create your views here.

class StudentDetails(APIView):
    permission_classes =[IsAuthenticated ,IsStudent]

    def get(self, request, *args,**kwargs):
        ''' Get the details of the perticular student'''
        print(request.user.id)
        student_data = Student.objects.get(user = request.user)
        serializer = StudentDataSerializer(student_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateSubjects(APIView):
    permission_classes = [IsAuthenticated,IsTeacher]

    def patch(self, request, *args,**kwargs):
        teacher_data = Teacher.objects.get(user = request.user)
        serializer = TeacherSerializer(teacher_data,data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class StudentsReport(TemplateView):
    ''' view to show students report'''
    template_name = "tulip_api_app/student_report.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student_details_from_db = Student.objects.all()  # getting all the students from database
        student_details = []  # initiating empty list to store below processed data
        if student_details_from_db:
            # creating list of all the subjects for the perticular student
            for student in student_details_from_db:
                temp_dict = {}
                subjects_list = []
                for teacher in student.student_teachers.all():
                    for sub in teacher.teacher_subjects.all():
                        subjects_list.append(sub.subject_name)

            # assigning other details of the student
                temp_dict["student_id"] = student.id
                temp_dict["student_name"] = student.student_name
                temp_dict["teachers"] = [tchr.teacher_name for tchr in student.student_teachers.all()]
                temp_dict["subjects"] = subjects_list

                student_details.append(temp_dict)

        context["student_details"] = student_details

        return context



