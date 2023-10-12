from rest_framework import serializers
# from store.models import TeamProfile,Service
from django.contrib.auth import authenticate

from store.serializer import SubjectSerializer
from .models import Account, Subject
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from urllib.parse import urljoin



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    


class LogoutSerializer(serializers.Serializer):
    pass




  

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
        password = self.validated_data["password"]

        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        else:
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

            user.set_password(validated_data["password"])
            user.role = "student"
            user.save()
            return user


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = (
#             "id",
#             "username",
#             "is_staff",
#             "last_login",
#             "over_view",
#             "work_time",
#             "is_admin",
#             "is_active",
#             #    'profile_pic',
#             "full_name",
#             "role",
#             "email",
#             "is_staff",
#             "address",
#             "phone",
#             "dob",
#             "work_time",
#             "date_joined",
#             "place",
#         )


# class EventManagementListSerializer(serializers.ModelSerializer):
#     profile = serializers.SerializerMethodField()
#     service = serializers.SerializerMethodField()
#     class Meta:
#         model = Account
#         fields = (
#             "id",
#             "team_name",
#             "username",
#             "email",
#             "phone",
#             "place",
#             "work_time",
#             "over_view",
#             "address",
#             # 'profile_pic'
#             "profile",
#             "service"
#         )
        
  
#     def get_profile(self, obj):
#         team_profile = TeamProfile.objects.filter(account=obj).first()
#         if team_profile:
#             url = team_profile.team_profile.url
#             if settings.MEDIA_URL in url:
#                 return urljoin(settings.HOSTNAME, url)
#         return None

#     def get_service(self, obj):
#         services = Service.objects.filter(account=obj).values()
#         return list(services)



#   def get_profile(self, obj):
#         request = self.context.get("request")
#         team_profile = TeamProfile.objects.filter(account=obj).first()
#         if team_profile and team_profile.team_profile:
#             url = team_profile.team_profile.url
#             if request:
#                 return request.build_absolute_uri(url)
#             else:
#                 return url
#         return None