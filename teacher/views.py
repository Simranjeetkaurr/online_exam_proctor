from questions.models import *
from django.contrib import messages
from django.shortcuts import render, redirect


def t_index(request):
    if request.method == 'POST':
        return create_category(request)
    else:
        data = Category.objects.all()
        return render(request, "teacher.html", {'data': data})



def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        try:
            # Create a new Category object
            category = Category(category_name=name, category_description=description)
            category.save()

            messages.success(request, 'Category created successfully.')  # Success message
            return redirect('teacher')  # Redirect to the teacher index page

        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name.') 
            return redirect('teacher')
            # You can also log the error if needed
            # logger.error(str(e))

    return render(request, 'teacher.html')