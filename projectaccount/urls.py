from . import views
from django.db import router
from django.urls import path
from rest_framework_nested import routers

from projectaccount.serializer import RegisterTeacherSerializer
from .views import (
    LoginView,
    LogoutView,
    # RegisterCustomerView,
    # RegisterEventTeamView,
    # ListUsersView,
    # EventManagementUsersView,
    
)



urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path("register/teacher", RegisterTeacherView.as_view(), name="register_teacher"),
    # path("register/student", RegisterStudentView.as_view(), name="registerstudent"),
    # path('register/teacher/<int:pk>', RegisterTeacherView.as_view(), name='user-detail'),

]

urlpatterns =  urlpatterns
# router = routers.DefaultRouter()
# router.register("register/teacher", views.RegisterTeacherView,basename="teacher"),
# # router.register("event_management_users", views.EventManagementUsersView)
# # router.register('eventteamlistsubcatagory',views.EventManagementSubcategoryViewSet,basename='MyModel')


# urlpatterns = router.urls + urlpatterns
