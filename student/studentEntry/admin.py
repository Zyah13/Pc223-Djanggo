from django.contrib import admin, messages
from django.db import IntegrityError, transaction
from .models import Course, Student
from .forms import StudentForm

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id' ,'course_name')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','id_number','full_name','gender','course','year_level','email_address')
    list_filter = ('gender', 'year_level')


    def full_name(self, obj):
        return f"{obj.lastname}, {obj.firstname} {obj.middle_initial}.  ".upper()
    full_name.short_description = 'Name'

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError:
            self.message_user(request, "A student with the same first and last name already exists.", messages.ERROR)

admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
