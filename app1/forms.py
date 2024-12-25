from django import forms
from .models import Student
from django.core.exceptions import ValidationError

# Form for creating and updating student records
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Link this form to the Student model
        fields = ['full_names', 'surname', 'gender', 'date_of_birth', 'email', 'mobile_number']  # Fields included in the form
        widgets = {
            # Use a date picker for the date_of_birth field for better user experience
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
        }

    # Custom validation for the mobile_number field
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if len(mobile_number) < 10:  # Ensure the mobile number is at least 10 digits long
            raise ValidationError("Mobile number is too short.")
        return mobile_number


# Form for student login
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class StudentLoginForm(forms.Form):
    # Field for entering the student's ID
    username = forms.CharField(
        max_length=6,  # Maximum length of the Student ID
        label="Student ID",  # Label displayed on the form
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Student ID'}),  # Placeholder text for the input field
    )
    # Field for entering the password
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),  # Use PasswordInput to hide input
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request  # Store the request object for authentication
        super().__init__(*args, **kwargs)

    # Custom validation for the login form
    def clean(self):
        username = self.cleaned_data.get('username')  # Retrieve the username from the form data
        password = self.cleaned_data.get('password')  # Retrieve the password from the form data
        if username and password:
            # Attempt to authenticate the user with the provided credentials
            self.user_cache = authenticate(
                request=self.request, username=username, password=password
            )
            if not self.user_cache:
                # Raise a validation error if authentication fails
                raise forms.ValidationError("Invalid Student ID or Password")
        return self.cleaned_data

    # Retrieve the authenticated user
    def get_user(self):
        return self.user_cache
