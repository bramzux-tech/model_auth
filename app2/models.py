from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator

class Staff(AbstractUser):
    # Personal Information
    full_names = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    # Gender choices
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

    # Mobile number with validation
    mobile_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid mobile number.")]
    )

    # Override groups and permissions
    groups = models.ManyToManyField(
        Group,
        related_name="staff_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="staff_users",
        blank=True
    )

    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    password = models.CharField(max_length=150, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set username to email
        self.username = self.email
        plain_password = self.password
        self.set_password(plain_password)  # Hash password
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_names} ({self.email})"
