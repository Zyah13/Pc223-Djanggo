from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_name = models.CharField(max_length=250, unique=True)


    def __str__(self):
        return self.course_name

class Student(models.Model):
    id_number = models.PositiveIntegerField(unique=True)
    lastname = models.CharField(max_length=50 )
    firstname = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(default=timezone.now) 
    email_address = models.EmailField(max_length=50, unique=True)
    YEAR_LEVEL_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    year_level = models.PositiveSmallIntegerField(choices=YEAR_LEVEL_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return f"{self.firstname} {self.middle_initial or ''} {self.lastname}"

    class Meta:
      unique_together = ('lastname', 'firstname')

    def save(self, *args, **kwargs):
        # Convert both first name and last name to lowercase for case-insensitive comparison
        self.firstname = self.firstname.upper()
        self.lastname = self.lastname.upper()
        super().save(*args, **kwargs)