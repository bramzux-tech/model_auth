from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator
import random

class Student(AbstractUser):
    # Automatically generated student_id
    student_id = models.CharField(max_length=6, unique=True, blank=True)

    # Personal Information
    full_names = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    # Gender choices: limited to specific values
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # Date of Birth
    date_of_birth = models.DateField()

    # Email (must be unique)
    email = models.EmailField(unique=True)

    # Mobile number with validation (accepts numbers with country code)
    mobile_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid mobile number.")]
    )

    # Override groups and permissions with custom related_name
    groups = models.ManyToManyField(
        Group,
        related_name="student_users",  # Unique related name for Student
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="student_users",
        blank=True
    )

    # Temporarily allow null for password and username
    password = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate student_id if it's not set
        if not self.student_id:
            self.student_id = f"ST{random.randint(1000, 9999)}"

        # Set username to student_id
        self.username = self.student_id

        # Automatically set password based on date of birth (in ddmmyy format)
        if not self.password and self.date_of_birth:
            dob_str = self.date_of_birth.strftime('%d%m%y')
            plain_password = f'student@{dob_str}'  # Generate the plain password
            print(f"Generated Password: {plain_password}")  # Debug: Print the password
            self.set_password(plain_password)  # Hash and set the password

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_names} ({self.student_id})"
