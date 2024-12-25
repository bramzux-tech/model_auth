from django.views.generic import ListView, CreateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, StudentLoginForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib import messages

# View for rendering the index page
class Index(View):
    def get(self, request, *args, **kwargs):
        # Render the `index.html` template
        return render(request, 'index.html')

# View for rendering the student home page
class StudentHomeView(View):
    def get(self, request, *args, **kwargs):
        # Render the `student_home.html` template
        return render(request, 'student_home.html')

# View for listing all students
class StudentListView(ListView):
    model = Student  # The model to retrieve student data
    template_name = "student_list.html"  # Template for displaying student list
    context_object_name = "students"  # Context name to use in the template
    # login_url = reverse_lazy('student_login')  # Optional: Redirects to login if required

# View for creating a new student
class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student  # The model for handling student data
    form_class = StudentForm  # Form used to create a new student
    template_name = "student_list.html"  # Template for creating students
    success_url = reverse_lazy("student_list")  # URL to redirect to after successful creation
    success_message = "Student created successfully."  # Success message displayed upon creation

    def form_valid(self, form):
        # Override the form validation to include additional functionality if needed
        response = super().form_valid(form)
        return response

# View for handling student login
class StudentLoginView(FormView):
    template_name = "student_login.html"  # Template for the login page
    form_class = StudentLoginForm  # Form used for student login
    success_url = reverse_lazy("student_home")  # URL to redirect to upon successful login

    def form_valid(self, form):
        # Handle successful login
        user = form.get_user()
        if user:
            # Log the user in
            login(self.request, user)
        return super().form_valid(form)

# View for handling student logout
class StudentLogoutView(View):
    def get(self, request):
        # Log the user out
        logout(request)
        messages.success(request, "You have been logged out.")  # Display logout success message
        return redirect("index")  # Redirect to the index page after logout
