from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Student

@receiver(post_migrate)
def create_student_group(sender, **kwargs):
    """
    Automatically creates the 'Students' group after migrations.
    """
    Group.objects.get_or_create(name='Students')


@receiver(post_save, sender=Student)
def add_to_student_group(sender, instance, created, **kwargs):
    """
    Adds a newly created Student to the 'Students' group.
    """
    if created:  # Only add to group when a new Student is created
        students_group, _ = Group.objects.get_or_create(name='Students')  # Ensure group exists
        instance.groups.add(students_group)
