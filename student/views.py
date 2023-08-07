from .models import *
from questions.models import *
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def st_index(request):
    # exams = Exam.objects.all()
    # Retrieve the courses that meet the filter conditions
    course = Acourse.objects.filter(isactive=True, isdeleted=False)
    # Filter the exams based on the active courses
    exams = Exam.objects.filter(courseid__in=course)
    examss=exams.order_by("-exam_start_date")
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
    return render(request, "student.html", {'data': page_obj})

def thankyou(request):
    return render(request, "thankyou.html")


def proctoring(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(question_exam=exam)
    questionss=questions.order_by("id")
    session_key = request.session.session_key
    paginator = Paginator(questionss, 1)
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

    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    
    total_null = Result.objects.filter(django_session=session_key, given_answer=None).count()
    if request.method == 'POST':
        for question in questions:
            question_id = str(question.id)
            selected_answer = request.POST.get('q' + question_id)
            correct_answer = question.correct_answer
            
            result, created = Result.objects.get_or_create(
                django_session=session_key,
                exam_id=exam,
                question_id=question,
                defaults={
                    'correct_answer': correct_answer,
                    'given_answer': selected_answer,
                    'marks_obtained': 1 if selected_answer == correct_answer else 0,
                    'total_attempt': 1
                }
            )

            if not created:
                result.correct_answer = correct_answer
                if selected_answer == None:
                    selected_answer = result.given_answer
                else:
                    selected_answer = selected_answer
                result.given_answer = selected_answer
                result.marks_obtained = 1 if selected_answer == correct_answer else 0
                result.attempt_date_time = timezone.now()
                result.total_attempt = result.total_attempt + 1
                result.save()
    total_null = paginator.num_pages - Result.objects.filter(django_session=session_key, given_answer=None).count()
        
    given_answers = Result.objects.filter(django_session=session_key).values('question_id', 'given_answer')
    given_answers_dict = {str(answer['question_id']): answer['given_answer'] for answer in given_answers}

    for question in page_obj:
        question_id = str(question.id)
        question.given_answer = given_answers_dict.get(question_id, None)
    
    context = {'data': page_obj, 'exam': exam,'null':total_null, 'answer': question.given_answer}
    
    return render(request, "proctoring.html", context)



