# from questions.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def t_index(request):
#     if request.method == 'POST':
#         return create_category(request)
#     else:
#         data = Category.objects.all()
#         datas=data.order_by("id")
#         paginator = Paginator(datas, 6)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         try:
#             page_obj = paginator.get_page(page_number)  # returns the desired page object
#         except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#             page_obj = paginator.page(1)
#         except EmptyPage:
#         # if page is empty then return last page
#             page_obj = paginator.page(paginator.num_pages)
#         return render(request, "teacher.html", {'data': page_obj})



# def create_category(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')

#         try:
#             # Create a new Category object
#             category = Category(category_name=name, category_description=description)
#             category.save()

#             messages.success(request, 'Category created successfully.')  # Success message
#             return redirect('teacher')  # Redirect to the teacher index page

#         except Exception as e:
#             messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name.')
#             return redirect('teacher')
#             # You can also log the error if needed
#             # logger.error(str(e))

#     return render(request, 'teacher.html')