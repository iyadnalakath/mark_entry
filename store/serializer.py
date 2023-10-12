from rest_framework import serializers
from projectaccount.models import Account, Subject
from store.models import Questions, SeriesExam, Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
    
class SeriesExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesExam
        fields = ('id', 'name')
    


class RegisterTeacherSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    class Meta:
        model = Account
        fields = ["id", "full_name", "username", "password", "subject"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        subject_id = validated_data.pop('subject', None)
        user = Account.objects.create(
            username=validated_data["username"],
            full_name=self.validated_data["full_name"],
            role="teacher",
        )
        user.set_password(validated_data["password"])

        if subject_id:
            user.subject_id = subject_id

        user.save()
        return user
    

    

class RegisterStudentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Student
        fields = [
            
            "name",
            "register_number",
            "roll_number"
        ]


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [

            'id',
            'student',
            'exam_name',
            'question_one',
            'question_one_co',
            'question_two',
            'question_two_co'
            'question_three',
            'question_three_co',
            'question_four',
            'question_four_co',
            'question_five',
            'question_five_co',
            'question_six',
            'question_six_co',
            'question_seven',
            'question_seven_co',
            'question_six',
            'question_six_co',
            'question_seven',
            'question_seven_co',
            'question_eight',
            'question_eight_co',
            'question_nine',
            'question_nine_co',
            'question_ten',
            'question_ten_co'
            
            ]
    
