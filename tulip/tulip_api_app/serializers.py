from rest_framework import serializers
from .models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "subject_name"]


class TeacherSerializer(serializers.ModelSerializer):
    '''Serializer to serialize Teacher Object '''
    teacher_subjects = SubjectSerializer(many=True,read_only=False)
    class Meta:
        model = Teacher
        fields = ["id", "teacher_name","teacher_subjects"]
    def update(self, instance, validated_data):
        ''' Implemented this method because serializes do not automatically update the data'''
        if validated_data:
            all_valid_subjects = [sub.subject_name for sub in Subject.objects.all()]
            subjects = validated_data.pop("teacher_subjects")
            already_assigned_subjects = [sub.subject_name for sub in instance.teacher_subjects.all()]
            print(already_assigned_subjects)
            for subject in subjects:
                if subject["subject_name"] not in already_assigned_subjects and subject["subject_name"] in all_valid_subjects:
                    instance.teacher_subjects.add(Subject.objects.get(subject_name=subject["subject_name"]))

            instance.save()   
        else:
            raise serializers.ValidationError('Please provide subjects to add ! in the format ex: {"teacher_subjects":[{"id":1,"subject_name":"Science"}]}')
        return instance




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "student_name","student_teachers"]

class StudentDataSerializer(serializers.ModelSerializer):
    student_teachers = TeacherSerializer(many=True, read_only=True)
    username = serializers.SerializerMethodField('find_username')
    def find_username(self,obj):
        return obj.user.username
    class Meta:
        model = Student
        fields = ["id", "student_name","username","student_teachers"]