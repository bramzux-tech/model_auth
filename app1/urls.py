from django.urls import path
from .views import StudentListView, StudentCreateView, StudentLoginView, StudentLogoutView, StudentHomeView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/create/", StudentCreateView.as_view(), name="student_create"),
    path('student_home/', StudentHomeView.as_view(), name='student_home'),
    path('student-login/', StudentLoginView.as_view(), name='student_login'),
    path('logout/', StudentLogoutView.as_view(), name='student_logout'),
]