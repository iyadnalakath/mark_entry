from rest_framework import serializers
from projectaccount.models import Account, Subject
from store.models import Questions, SeriesExam, Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name','code')
    
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
    def update(self, instance, validated_data):
        # Update username, full_name, password, copy_pass, and subject fields
        instance.username = validated_data.get('username', instance.username)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            instance.copy_pass = password  # Update copy_pass field

        subject = validated_data.get('subject')
        if subject:
            instance.subject = subject
                
        instance.save()
        return instance


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

    student_name = serializers.CharField(source="student.name", read_only=True)
    total_mark = serializers.SerializerMethodField() 

    class Meta:
        model = Questions
        fields = [

            'id',
            'teacher',
            'exam_name',
            'student',
            'student_name',
            'question_1',
            'question_one_co',
            'question_2',
            'question_two_co',
            'question_3',
            'question_three_co',
            'question_4',
            'question_four_co',
            'question_5',
            'question_five_co',
            'question_6',
            'question_six_co',
            'question_7',
            'question_seven_co',
            'question_8',
            'question_eight_co',
            'question_9',
            'question_nine_co',
            'question_10',
            'question_ten_co',
            'total_mark'

            ]
    
    def get_total_mark(self, obj):
        question_1 = obj.question_1 or 0
        question_2 = obj.question_2 or 0
        question_3 = obj.question_3 or 0
        question_4 = obj.question_4 or 0
        question_5 = obj.question_5 or 0
        question_6 = obj.question_6 or 0
        question_7 = obj.question_7 or 0
        question_8 = obj.question_8 or 0
        question_9 = obj.question_9 or 0
        question_10 = obj.question_10 or 0
        

        total_marks = question_1 + question_2 + question_3 + question_4 +question_5 + question_6 + question_7 + question_8 + question_9 + question_10
        return total_marks