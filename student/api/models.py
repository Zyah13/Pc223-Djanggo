from django.db import models
from tastypie.resources import ModelResource
from studentEntry.models import Student



class StudentResource(ModelResource):
 class Meta:
    queryset = Student.objects.all()
    resource_name = 'studentEntry'