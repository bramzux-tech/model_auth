# Generated by Django 4.2.14 on 2024-12-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='password',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
