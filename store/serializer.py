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
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    password = serializers.CharField(write_only=True)
    copy_pass = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ["id", "full_name", "username", "password", "subject", "subject_name", "copy_pass"]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def create(self, validated_data):
        subject = validated_data.pop('subject', None)
        password = validated_data.pop('password')  
        user = Account.objects.create(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            role="teacher",
            copy_pass=password,  # Set copy_pass here
        )
        user.set_password(password)  

        if subject:
            user.subject = subject
        
        user.save()

        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
        return ret

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
    #     return ret


class RegisterStudentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "register_number",
            "roll_number"
        ]


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [

            'id',
            'teacher',
            'exam_name',
            'student',
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
    
