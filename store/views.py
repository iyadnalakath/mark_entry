from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from projectaccount.models import Account, Subject

from store.models import Questions, SeriesExam, Student
from store.serializer import QuestionsSerializer, SeriesExamSerializer, SubjectSerializer,RegisterTeacherSerializer,RegisterStudentSerializer

# Create your views here.




class SubjectViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SeriesExamViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SeriesExam.objects.all()
    serializer_class = SeriesExamSerializer


class TeacherRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Account.objects.all()
    serializer_class = RegisterTeacherSerializer

    def get_queryset(self):
        return Account.objects.filter(role="teacher")

class StudentRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = RegisterStudentSerializer



class StudentRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = RegisterStudentSerializer

class QuestionView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer




