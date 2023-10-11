



from rest_framework import serializers
from projectaccount.models import Account
from store.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
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
        model = Account
        fields = [
            
            "username",
            "register_number",
            "roll_number"
        ]

        # read_only_fields = ("password2",)

        # extra_kwargs = {
        #     "password": {"write_only": True},
        #     # 'password2':{'write_only':True}
        # }

    def create(self, validated_data):


        user = Account.objects.create(
            username=validated_data["username"],
            register_number=validated_data["register_number"],
            roll_number=validated_data["roll_number"],
                # email=validated_data["email"],
                # team_name=self.validated_data["team_name"],
                # phone=self.validated_data["phone"],
                # profile_pic=self.validated_data['profile_pic']
                # password=self.validated_data["password"],
        )

        # user.set_password(validated_data["password"])
        user.role = "student"
        user.save()
        return user

