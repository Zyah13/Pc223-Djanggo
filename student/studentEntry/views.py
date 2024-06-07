from django.shortcuts import render
from .models import Student
from .forms import StudentForm
import os
from django.conf import settings
import uuid
from PIL import Image 
from django.db.models import Q
from django.db import IntegrityError

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(id_number__icontains=q) |Q(firstname__icontains=q) |Q(lastname__icontains=q) |Q(course__course_name__icontains=q))
        students = Student.objects.filter(search)
    else:
       students = Student.objects.all()
    return render(request, 'studentEntry/index.html', { 'studentEntry': students })


def detail(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'studentEntry/detail.html', { 'student': student })


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            new_id_number = form.cleaned_data['id_number']
            new_lastname = form.cleaned_data['lastname']
            new_firstname = form.cleaned_data['firstname']
            new_middle_initial = form.cleaned_data['middle_initial']
            new_gender = form.cleaned_data['gender']
            new_birthdate = form.cleaned_data['birthdate']
            new_email_address = form.cleaned_data['email_address']
            new_year_level = form.cleaned_data['year_level']
            new_course = form.cleaned_data['course']
            new_image = form.cleaned_data['image']

            image_extension = os.path.splitext(new_image.name)[1].lower()
            valid_image_formats = [".jpg", ".jpeg", ".png", ".gif"]
            
      
            if image_extension not in valid_image_formats:
                error_message = "Invalid image format. Only JPG, JPEG, PNG, or GIF are allowed."
                return render(request, 'studentEntry/add.html', {
                    'form': form,
                    'error_message': error_message
                })

            img = Image.open(new_image)
            width, height = img.size
            if (width != 600 or height != 600) and (width != 120 or height != 120) and (width != 1200 or height != 1200):
                error_message = "Invalid image size. Please upload an image that is either 2x2 inches (120x120 pixels | 1200x1200) or 600x600 pixels."
                return render(request, 'studentEntry/add.html', {
                    'form': form,
                    'error_message': error_message
                })

            unique_filename = str(uuid.uuid4()) + image_extension
            image_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

            with open(image_path, "wb") as f:
                for chunk in new_image.chunks():
                    f.write(chunk)

            try:
             new_student = Student(
                id_number=new_id_number,
                lastname=new_lastname,
                firstname=new_firstname,
                middle_initial=new_middle_initial,
                gender=new_gender,
                birthdate=new_birthdate,
                email_address=new_email_address,
                year_level=new_year_level,
                course=new_course,
                image=unique_filename  
             )
             new_student.save()

             return render(request, 'studentEntry/add.html', {
                'form': StudentForm(),
                'success': True
             })
            except IntegrityError:
             error_message = "The student already exists."
             return render(request, 'studentEntry/add.html', {
                    'form': form,
                    'error_message': error_message
                })
    else:
        form = StudentForm()

    return render(request, 'studentEntry/add.html', {
        'form': form
    })
