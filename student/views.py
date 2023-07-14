from django.shortcuts import render
from questions.models import *
from django.shortcuts import render, redirect, get_object_or_404


def st_index(request):
    exams = Exam.objects.all()
    return render(request, "student.html", {'data': exams})



def test(request):
    return render(request, "test.html")

# =============== 
# def exam_attempt(request, exam_id):
#     exam = get_object_or_404(Exam, id=exam_id)
#     questions = Question.objects.filter(question_exam=exam)
#     if request.method == 'POST':
#         student = request.user  # Assuming the user is logged in
#         score = 0

#         for question in questions:
#             answer = request.POST.get(f"answer_{question.id}")

#             if answer == question.correct_answer:
#                 score += 1

#         attempt = ExamAttempt(exam=exam, student=student, score=score)
#         attempt.save()

#         # Optionally, you can redirect the user to a results page
#         # return redirect(reverse('exam_results', args=[attempt.id]))

#     return render(request, 'exam_attempt.html', {'exam': exam, 'questions': questions})




# ==============================

