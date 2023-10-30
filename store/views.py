from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from projectaccount.models import Account, Subject
from store.models import Questions, SeriesExam, Student
from store.serializer import QuestionsSerializer, SeriesExamSerializer, SubjectSerializer,RegisterTeacherSerializer,RegisterStudentSerializer
from rest_framework.response import Response
from rest_framework import status

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



# class StudentRegistrationView(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Student.objects.all()
#     serializer_class = RegisterStudentSerializer

class QuestionView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if self.request.user.role == "teacher":
            if self.request.GET.get("exam_name"):
                exam_name = self.request.GET.get("exam_name")
                queryset = queryset.filter(exam_name=exam_name)

            queryset = queryset.filter(teacher=self.request.user.id)
            serializer = QuestionsSerializer(
                queryset, many=True, context={"request": self.request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return super().list(request, *args, **kwargs)
        

        

    def create(self, request, *args, **kwargs):
        data_list = request.data
        responses = []

        for data in data_list:
            student_id = data.get('student')
            exam_name_id = data.get('exam_name')
            if student_id:
                existing_record = Questions.objects.filter(student=student_id , exam_name=exam_name_id).first()
                if existing_record:
                    serializer = self.get_serializer(existing_record, data=data)
                else:
                    serializer = self.get_serializer(data=data)
            else:
                serializer = self.get_serializer(data=data)

            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            responses.append(serializer.data)

        return Response(responses, status=status.HTTP_201_CREATED)


