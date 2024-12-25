from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Staff
from .forms import StaffForm, StaffLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

# View for rendering the home page for staff
class StaffHomeView(View):
    def get(self, request, *args, **kwargs):
        # Render the `staff_home.html` template
        return render(request, 'staff_home.html')

# View for listing all staff members
class StaffListView(ListView):
    model = Staff  # The Staff model to retrieve data from
    template_name = "staff_list.html"  # Template used for displaying the list
    context_object_name = "staff_list"  # Context name to use in the template

# View for creating a new staff member
class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Staff  # The Staff model for handling staff data
    form_class = StaffForm  # Form used to create a new staff member
    template_name = "staff_list.html"  # Template used for creating staff
    success_url = reverse_lazy("staff_list")  # URL to redirect to upon success
    success_message = "Staff member created successfully."  # Message displayed after successful creation

    def get_context_data(self, **kwargs):
        # Adds additional context to the template, including all staff
        context = super().get_context_data(**kwargs)
        context["staff_list"] = Staff.objects.all()
        return context

# View for staff login
class StaffLoginView(View):
    form_class = StaffLoginForm  # Form used for staff login
    template_name = "staff_login.html"  # Template used for the login page

    def get(self, request):
        # Handles GET requests by rendering the login form
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        # Handles POST requests for staff login
        form = self.form_class(request.POST)
        if form.is_valid():
            # Get the username (email) and password from the form
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Authenticate the user using the custom authentication backend
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:  # Check if the account is active
                    login(request, user)  # Log the user in
                    messages.success(request, "Login successful.")  # Success message
                    return redirect("staff_home")  # Redirect to the staff home page
                else:
                    # If the account is inactive, display an error message
                    messages.error(request, "Account is inactive.")
            else:
                # If credentials are invalid, display an error message
                messages.error(request, "Invalid credentials.")
        return render(request, self.template_name, {"form": form})

# View for staff logout
class StaffLogoutView(View):
    def get(self, request):
        # Logs the user out and displays a success message
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("index")  # Redirect to the index page
