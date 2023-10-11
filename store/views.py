from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from projectaccount.models import Account

from store.models import Subject
from store.serializer import SubjectSerializer,RegisterTeacherSerializer,RegisterStudentSerializer

# Create your views here.




class SubjectViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = RegisterTeacherSerializer



class StudentRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = RegisterStudentSerializer



