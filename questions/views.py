import base64
import csv

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
# from sklearn.setup import configuration
from .models import *
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Acourse, Exam, Question,Configuration


#  Courses Code starts here!

# def courses(request):
#     # Get active and non-deleted courses
#     courses = Acourse.objects.filter(isactive=True, isdeleted=False).order_by('courseid')


#     # programtype = Acourse.objects.get(programtype)
#     # configurations = Configuration.objects.get(configurationid=course.programtype)
#     # programtype = Configuration.objects.get(configuration)
#     # configurations = Configuration.objects.values('configurationid', 'value')


#     # Pagination
#     paginator = Paginator(courses, 6)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     try:
#         page_obj = paginator.get_page(page_number)  # returns the desired page object
#     except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         # if page is empty then return last page
#         page_obj = paginator.page(paginator.num_pages)

#     # Fetching the configuration names for coursesession and programtype
#     for course in page_obj:
#         try:
#             session_config = Configuration.objects.get(configurationid=course.coursesession)
#             course.coursesession = session_config.value
#         except Configuration.DoesNotExist:
#             pass

#         try:
#             program_config = Configuration.objects.get(configurationid=course.programtype)
#             course.programtype = program_config.value
#         except Configuration.DoesNotExist:
#             pass

#     context = {
#         'data': page_obj,
#     }
    
#     return render(request, 'courses.html', context)

#  Courses Code ends here!

# def courses(request):
#     # Get active and non-deleted courses
#     courses = Acourse.objects.filter(isactive=True, isdeleted=False).order_by('courseid')

#     # Pagination
#     paginator = Paginator(courses, 6)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     try:
#         page_obj = paginator.get_page(page_number)  # returns the desired page object
#     except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         # if page is empty then return last page
#         page_obj = paginator.page(paginator.num_pages)

#     # Fetching the configuration names, IDs, and values for coursesession and programtype
#     for course in page_obj:
#         try:
#             session_config = Configuration.objects.get(configurationid=course.coursesession)
#             course.coursesession_id = session_config.configurationid  # Add the ID to the course object
#             course.coursesession_value = session_config.value  # Add the value to the course object
#         except Configuration.DoesNotExist:
#             pass

#         try:
#             program_config = Configuration.objects.get(configurationid=course.programtype)
#             course.programtype_id = program_config.configurationid  # Add the ID to the course object
#             course.programtype_value = program_config.value  # Add the value to the course object
#         except Configuration.DoesNotExist:
#             pass

#     context = {
#         'data': page_obj,
#     }
    
#     return render(request, 'courses.html', context)

def courses(request):
    # Get active and non-deleted courses
    courses = Acourse.objects.filter(isactive=True, isdeleted=False).order_by('courseid')

    # Pagination
    paginator = Paginator(courses, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    # Fetching the configuration names, IDs, and values for coursesession and programtype
    for course in page_obj:
        try:
            session_config = Configuration.objects.get(configurationid=course.coursesession)
            course.coursesession_id = session_config.configurationid  # Add the ID to the course object
            course.coursesession_value = session_config.value  # Add the value to the course object
        except Configuration.DoesNotExist:
            pass

        try:
            program_config = Configuration.objects.get(configurationid=course.programtype)
            course.programtype_id = program_config.configurationid  # Add the ID to the course object
            course.programtype_value = program_config.value  # Add the value to the course object
        except Configuration.DoesNotExist:
            pass

    # Fetch Configuration objects for options
    configurations = Configuration.objects.all()

    context = {
        'data': page_obj,
        'configurations': configurations,  # Add the configurations variable to the context
    }
    
    return render(request, 'courses.html', context)

def course_detail(request,courseid):
    course = get_object_or_404(Acourse, courseid=courseid)
    session_config = Configuration.objects.get(configurationid=course.coursesession)
    course.coursesession = session_config.value
    program_config = Configuration.objects.get(configurationid=course.programtype)
    course.programtype = program_config.value
    
    if request.method == 'POST':
        course_id = courseid
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        start_date = request.POST.get('date')
        # Retrieve the selected course
        course = Acourse.objects.get(courseid=course_id)

        # Create a new Exam object
        try:
            exam = Exam(courseid=course, exam_name=name, exam_start_date=start_date,
                        exam_description=description, exam_duration=duration)
            exam.save()
            # Success message
            messages.success(request, 'Exam created successfully.')
            return redirect('course_detail',courseid=courseid)
        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect('course_detail', courseid=courseid)
    
    exams = Exam.objects.filter(courseid=course)
    examss=exams.order_by('-exam_start_date')
    paginator = Paginator(examss, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    
    context = {'data': course,'exams': page_obj}
    return render(request, 'course.html', context)

# #course details ends here

#  testing code
# def courses(request):
    courses = Acourse.objects.filter(isactive=True, isdeleted=False)
    datas = courses.order_by('courseid')
    paginator = Paginator(datas, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    # Fetching the configuration names for coursesession and programtype
    for course in page_obj:
        try:
            session_config = Configuration.objects.get(configurationid=course.coursesession)
            course.coursesession = session_config.value
        except Configuration.DoesNotExist:
            pass

        try:
            program_config = Configuration.objects.get(configurationid=course.programtype)
            course.programtype = program_config.value
        except Configuration.DoesNotExist:
            pass

    context = {
        'data': page_obj,
    }
    
    return render(request, 'courses.html', context)
#  testing code ends here
# exam start

def exams(request):
    exam = Exam.objects.all()
    # Retrieve the courses that meet the filter conditions
    course = Acourse.objects.filter(isactive=True, isdeleted=False)

    # Filter the exams based on the active courses
    data = Exam.objects.filter(courseid__in=course)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        start_date = request.POST.get('date')
        # Retrieve the selected course
        course = Acourse.objects.get(courseid=course_id)

        # Create a new Exam object
        try:
            exam = Exam(courseid=course, exam_name=name, exam_start_date=start_date,
                        exam_description=description, exam_duration=duration)
            exam.save()
            # Success message
            messages.success(request, 'Exam created successfully.')
            return redirect('exams')
        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect('exams')
    datas=data.order_by('id')
    paginator = Paginator(datas, 6)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    return render(request, "exams.html", {'data': page_obj, 'course': course})



def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    course=Acourse.objects.get(courseid=exam.courseid_id)
    session_config = Configuration.objects.get(configurationid=course.coursesession)
    course.coursesession = session_config.value
    program_config = Configuration.objects.get(configurationid=course.programtype)
    course.programtype = program_config.value
    questions = Question.objects.filter(question_exam=exam)
    if request.method == 'POST' and 'update_exam' in request.POST:
        name = request.POST.get('name')
        description = request.POST.get('description','')
        duration = request.POST.get('duration')
        start_date = request.POST.get('date')

        # Update the exam
        try:
            exam.exam_name = name
            exam.exam_description = description
            exam.exam_duration = duration
            exam.exam_start_date = start_date
            exam.save()
            messages.success(request, 'Exam Updated successfully.')
            return redirect(reverse('exam_detail', args=[exam_id]))

        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect(reverse('exam_detail', args=[exam_id]))
        
    elif request.method == 'POST' and 'create_question' in request.POST:
        exam_id = exam_id
        name = request.POST.get('name')
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')

        # Retrieve the selected exam
        exam = Exam.objects.get(id=exam_id)

        # Create a new Question object
        try:
            question = Question(question_exam=exam, question_name=name, question_text=question,
                                option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=answer)
            question.save()
            # Success message
            messages.success(request, 'Question created successfully.')
            return redirect('exam_detail',exam_id=exam_id)
        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect('exam_detail', exam_id=exam_id)
    
    
    
    questionss=questions.order_by('id')
    paginator = Paginator(questionss, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'exam.html', {'questions': page_obj, 'exam': exam, 'course': course})


def exam_delete(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    return redirect(reverse('exams'))

# exam end


# question start

# def questions(request):
    course=Acourse.objects.filter(isactive=True, isdeleted=False)
    exam = Exam.objects.filter(courseid__in=course)
    data = Question.objects.filter(question_exam__in=exam)
    
    
    
    if request.method == 'POST':
        exam_id = request.POST.get('exam')
        name = request.POST.get('name')
        question = request.POST.get('question')
        image= request.FILES.get('image')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')

        # Retrieve the selected exam
        exam = Exam.objects.get(id=exam_id)
        
        
        if image is None:
            base64_image = ''
        else:    
            with image.open('rb') as img_file:
                base64_image = base64.b64encode(img_file.read()).decode('utf-8')
                
        
        # Create a new Question object
        try:
            question = Question(question_exam=exam, question_name=name, question_text=question,question_image=base64_image,
                                option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=answer)
            question.save()
            # Success message
            messages.success(request, 'Question created successfully.')
            return redirect('questions')
        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect('questions')
    datas=data.order_by('id')
    paginator = Paginator(datas, 13)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    return render(request, "questions.html", {'data': page_obj, 'exam': exam})

# Single question ends=====>  

def questions(request):
    course = Acourse.objects.filter(isactive=True, isdeleted=False)
    exam = Exam.objects.filter(courseid__in=course)
    data = Question.objects.filter(question_exam__in=exam)

    if request.method == 'POST':
        if 'create_question' in request.POST:
            exam_id = request.POST.get('exam')
            name = request.POST.get('name')
            question = request.POST.get('question')
            image = request.FILES.get('image')
            option1 = request.POST.get('option1')
            option2 = request.POST.get('option2')
            option3 = request.POST.get('option3')
            option4 = request.POST.get('option4')
            answer = request.POST.get('answer')

            # Retrieve the selected exam
            exam = Exam.objects.get(id=exam_id)

            if image is None:
                base64_image = ''
            else:
                with image.open('rb') as img_file:
                    base64_image = base64.b64encode(img_file.read()).decode('utf-8')

            # Create a new Question object
            try:
                question_obj = Question(question_exam=exam, question_name=name, question_text=question,
                                        question_image=base64_image,
                                        option1=option1, option2=option2, option3=option3, option4=option4,
                                        correct_answer=answer)
                question_obj.save()
                # Success message
                messages.success(request, 'Question created successfully.')
                return redirect('questions')
            except Exception as e:
                messages.error(
                    request, f'Error occurred: {str(e)}, Kindly choose another name.')
                return redirect('questions')

        elif 'upload_csv' in request.POST and request.FILES.get('csv_file'):
            csv_file = request.FILES.get('csv_file')
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(decoded_file)
                
                if request.method == 'POST':
                    # Retrieve the selected exam ID from the dropdown
                    selected_exam = request.POST.get('exam')

                try:
                    exam = Exam.objects.get(id=selected_exam)
                except Exam.DoesNotExist:
                    messages.error(
                    request, f'Error occurred while processing the CSV file: Exam with ID {selected_exam} does not exist.')
                    return redirect('questions')

                for row in csv_reader:
                    name = row['name']
                    question_text = row['question']
                    image = row['image']
                    option1 = row['option1']
                    option2 = row['option2']
                    option3 = row['option3']
                    option4 = row['option4']
                    answer = row['answer']

                    if image:
                        with open(image, 'rb') as img_file:
                            base64_image = base64.b64encode(
                            img_file.read()).decode('utf-8')
                    else:
                        base64_image = ''

                    question_obj = Question(question_exam=exam, question_name=name, question_text=question_text,
                                        question_image=base64_image,
                                        option1=option1, option2=option2, option3=option3, option4=option4,
                                        correct_answer=answer)
                    question_obj.save()
                messages.success(request, 'Questions created successfully from the CSV file.')
                return redirect('questions')
            except Exception as e:
                messages.error(request, f'Error occurred while processing the CSV file: {str(e)}')
                return redirect('questions')


    datas = data.order_by('id')
    paginator = Paginator(datas, 13)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "questions.html", {'data': page_obj, 'exam': exam})


#  =========================
def question_detail_edit(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    # Assuming 'question_exam' is the foreign key to the Exam model
    exam = question.question_exam
    questions = Question.objects.filter(question_exam=exam)

    if request.method == 'POST':
        name = request.POST.get('name')
        question_text = request.POST.get('question','')
        image= request.FILES.get('image')

        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')
         
        if image is None and question.question_image is not None:
            base64_image = question.question_image
        elif image is None and question.question_image is None:
            base64_image = ''
        else:    
            with image.open('rb') as img_file:
                base64_image = base64.b64encode(img_file.read()).decode('utf-8')
        # with image.open('rb') as img_file:
        #         base64_image = base64.b64encode(img_file.read()).decode('utf-8')
        # Update the question
        try:
            question.question_name = name
            question.question_text = question_text
            question.question_image=base64_image
            question.option1 = option1
            question.option2 = option2
            question.option3 = option3
            question.option4 = option4
            question.correct_answer = answer
            question.save()
            messages.success(request, 'Question Updated successfully.')
            return redirect(reverse('question_detail', args=[question_id]))

        except Exception as e:
            messages.error(
                request, f'Error occurred: {str(e)}, Kindly Choose another name ')
            return redirect(reverse('question_detail', args=[question_id]))
    questionss = questions.order_by('id')
    paginator = Paginator(questionss, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'question.html', {'question': question, 'questions': page_obj})


def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect(reverse('questions'))

# question end


