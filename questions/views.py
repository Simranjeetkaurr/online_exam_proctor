from .models import *
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


# category start
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    courses = Course.objects.filter(course_category=category)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        # Update the category
        try:
            category.category_name = name
            category.category_description = description
            category.save()
            
            messages.success(request, 'Category Updated successfully.')
            return redirect(reverse('category_detail', args=[category_id]))
        
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect(reverse('category_detail', args=[category_id]))

    return render (request, 'category.html', {'category': category, 'courses': courses})



def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect(reverse('teacher'))

# category end

# course start
def courses(request):
    data = Course.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image','')

        # Retrieve the selected category
        categori = Category.objects.get(id=category_id)

        # Create a new Course object
        try:
            course = Course(course_category=categori, course_name=name, course_description=description, course_image=image)
            course.save()
            messages.success(request, 'Course created successfully.')  # Success message
            return redirect('courses')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect('courses')

    return render(request, 'courses.html', {'category': category, 'data': data})

def course_detail(request, course_id):
    courses = get_object_or_404(Course, id=course_id)
    exams = Exam.objects.filter(exam_course=courses)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image','')
        # Retrieve the selected category

        # Update the course
        try:
            courses.course_name = name
            courses.course_description = description
            courses.course_image = image
            
            courses.save()
            messages.success(request, 'Course Updated successfully.')
            return redirect(reverse('course_detail', args=[course_id]))
        
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect(reverse('course_detail', args=[course_id]))

    return render(request, 'course.html', {'exams': exams, 'courses': courses})




def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect(reverse('courses'))

# course end

# exam start
def exams(request):
    data= Exam.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        course_id = request.POST.get('course')
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        start_date = request.POST.get('date')

        # Retrieve the selected course
        course = Course.objects.get(id=course_id)

        # Create a new Exam object
        try:
            exam = Exam(exam_course=course, exam_name=name,exam_start_date=start_date, exam_description=description, exam_duration=duration)
            exam.save()
            messages.success(request, 'Exam created successfully.')  # Success message
            return redirect('exams')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect('exams')

        
    return render(request, "exams.html",{'data':data, 'course': course})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(question_exam=exam)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
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
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect(reverse('exam_detail', args=[exam_id]))

        

    return render(request, 'exam.html', {'questions': questions, 'exam': exam})


def exam_delete(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    return redirect(reverse('exams'))

# exam end


# question start
def questions(request):
    data= Question.objects.all()
    exam = Exam.objects.all()
    if request.method == 'POST':
        exam_id = request.POST.get('exam')
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
            question = Question(question_exam=exam, question_name=name, question_text=question, option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=answer)
            question.save()
            messages.success(request, 'Question created successfully.')  # Success message
            return redirect('questions')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect('questions')
    return render(request, "questions.html",{'data':data, 'exam': exam})

def question_detail_edit(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    exam = question.question_exam  # Assuming 'question_exam' is the foreign key to the Exam model
    questions = Question.objects.filter(question_exam=exam)

    if request.method == 'POST':
        name = request.POST.get('name')
        question_text = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')

        # Update the question
        try:
            question.question_name = name
            question.question_text = question_text
            question.option1 = option1
            question.option2 = option2
            question.option3 = option3
            question.option4 = option4
            question.correct_answer = answer
            question.save()
            messages.success(request, 'Question Updated successfully.')
            return redirect(reverse('question_detail', args=[question_id]))
        
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}, Kindly Choose another name ') 
            return redirect(reverse('question_detail', args=[question_id]))
    return render(request, 'question.html', {'question': question, 'questions': questions})



def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect(reverse('questions'))

# question end



def exam_attempt(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(question_exam=exam)

    if request.method == 'POST':
        user = request.user
        attempt = ExamAttempt(user=user, exam=exam)
        attempt.save()

        question_ids = set()

        for question in questions:
            answer = request.POST.get(f'question_{question.id}')

            if question.id in question_ids:
                messages.error(request, 'Each question should have a unique answer.')
                return redirect('exam_attempt', exam_id=exam_id)

            question_ids.add(question.id)

            user_answer = UserAnswer(exam_attempt=attempt, question=question, answer=answer)
            user_answer.save()

        attempt.calculate_score()
        messages.success(request, 'Exam submitted successfully.')
        return redirect('exam_result', attempt_id=attempt.id)

    return render(request, 'exam_attempt.html', {'exam': exam, 'questions': questions})


def exam_result(request, attempt_id):
    attempt = get_object_or_404(ExamAttempt, id=attempt_id)
    return render(request, 'exam_result.html', {'attempt': attempt})