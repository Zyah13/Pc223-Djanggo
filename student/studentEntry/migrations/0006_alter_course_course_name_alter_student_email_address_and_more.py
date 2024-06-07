# Generated by Django 5.0.6 on 2024-05-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentEntry', '0005_alter_student_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_address',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
