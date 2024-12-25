from django import forms
from .models import Staff
from django.core.exceptions import ValidationError

# Form for creating and updating staff members
class StaffForm(forms.ModelForm):
    # Field to confirm the password during creation
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Staff  # Links the form to the Staff model
        fields = [
            'full_names', 'surname', 'gender', 'date_of_birth',
            'email', 'mobile_number', 'password', 'password_confirm'
        ]
        widgets = {
            # Use PasswordInput for password fields to hide input
            'password': forms.PasswordInput,
            # Use a datepicker for date_of_birth field for better user experience
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
        }

    # Validation for the mobile number field
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if len(mobile_number) < 10:  # Ensure mobile number is at least 10 digits
            raise ValidationError("Mobile number is too short.")
        return mobile_number

    # Custom clean method to validate password confirmation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        # Check if password and password_confirm match
        if password != password_confirm:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data

# Form for staff login
class StaffLoginForm(forms.Form):
    # Field for entering the staff email (username)
    username = forms.CharField(
        max_length=255,
        label="Staff email",  # Field label displayed to users
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),  # Placeholder for better UX
    )
    # Field for entering the password
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})  # Use PasswordInput to hide input
    )
