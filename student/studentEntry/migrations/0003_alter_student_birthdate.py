# Generated by Django 5.0.6 on 2024-05-19 19:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentEntry', '0002_alter_student_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
