from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Staff

@receiver(post_migrate)
def create_staff_group(sender, **kwargs):
    """
    Automatically creates the 'Staffs' group after migrations.
    """
    Group.objects.get_or_create(name='Staffs')


@receiver(post_save, sender=Staff)
def add_to_staff_group(sender, instance, created, **kwargs):
    """
    Adds a newly created Staff to the 'Staffs' group.
    """
    if created:  # Only add to group when a new Staff is created
        staffs_group, _ = Group.objects.get_or_create(name='Staffs')  # Ensure group exists
        instance.groups.add(staffs_group)
