from django.urls import path
from .views import StaffListView, StaffCreateView, StaffLoginView, StaffLogoutView

urlpatterns = [
    path("staffs/", StaffListView.as_view(), name="staff_list"),
    path("staff-create/", StaffCreateView.as_view(), name="staff_create"),
    path("staff-login/", StaffLoginView.as_view(), name="staff_login"),
    path('logout/', StaffLogoutView.as_view(), name='staff_logout'),
]
