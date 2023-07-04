# from django import forms
# from .models import Question

# def exam_attempt(request, exam_id):
#     exam = get_object_or_404(Exam, id=exam_id)
#     questions = Question.objects.filter(question_exam=exam)

#     if request.method == 'POST':
#         form = ExamAttemptForm(request.POST)

#         if form.is_valid():
#             user = request.user
#             attempt = ExamAttempt(user=user, exam=exam)
#             attempt.save()

#             for question in questions:
#                 answer = request.POST.get(f'question_{question.id}')
#                 user_answer = UserAnswer(exam_attempt=attempt, question=question, answer=answer)
#                 user_answer.save()

#             attempt.calculate_score()
#             messages.success(request, 'Exam submitted successfully.')
#             return redirect('exam_result', attempt_id=attempt.id)
#     else:
#         form = ExamAttemptForm()

#     return render(request, 'exam_attempt.html', {'exam': exam, 'questions': questions, 'form': form})

# def exam_result(request, attempt_id):
#     attempt = get_object_or_404(ExamAttempt, id=attempt_id)
#     return render(request, 'exam_result.html', {'attempt': attempt})


# class ExamAttemptForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         questions = kwargs.pop('questions')
#         super(ExamAttemptForm, self).__init__(*args, **kwargs)

#         for question in questions:
#             choices = [(f'option_{i}', getattr(question, f'option{i}')) for i in range(1, 5)]
#             self.fields[f'question_{question.id}'] = forms.ChoiceField(label=question.question_text, choices=choices, widget=forms.RadioSelect)

#     def clean(self):
#         cleaned_data = super().clean()
#         question_ids = set()

#         for field_name, _ in self.fields.items():
#             if field_name.startswith('question_'):
#                 question_id = int(field_name.split('_')[1])
#                 if question_id in question_ids:
#                     raise forms.ValidationError('Each question should have a unique answer.')
#                 question_ids.add(question_id)

#         return cleaned_data




# from django.shortcuts import render, get_object_or_404
# from .models import Exam, Question

# def exam_attempt(request, exam_id):
#     exam = get_object_or_404(Exam, id=exam_id)
#     questions = Question.objects.filter(question_exam=exam)

#     if request.method == 'POST':
#         total_questions = len(questions)
#         correct_answers = 0

#         for question in questions:
#             answer_field_name = f'question_{question.id}'
#             selected_answer = request.POST.get(answer_field_name)

#             if selected_answer == question.correct_answer:
#                 correct_answers += 1

#         percentage = (correct_answers / total_questions) * 100

#         # Render the result page
#         return render(request, 'result.html', {
#             'exam': exam,
#             'total_questions': total_questions,
#             'correct_answers': correct_answers,
#             'percentage': percentage
#         })

#     return render(request, 'exam_attempt.html', {
#         'exam': exam,
#         'questions': questions
#     })
    

# def exam_attempt(request, exam_id):
#     exam = get_object_or_404(Exam, id=exam_id)
#     questions = Question.objects.filter(question_exam=exam)

#     if request.method == 'POST':
#         user = request.user
#         attempt = ExamAttempt(user=user, exam=exam)
#         attempt.save()

#         question_ids = set()

#         for question in questions:
#             answer = request.POST.get(f'question_{question.id}')

#             if question_id in question_ids:
#                 messages.error(request, 'Each question should have a unique answer.')
#                 return redirect('exam_attempt', exam_id=exam_id)

#             question_ids.add(question_id)

#             user_answer = UserAnswer(exam_attempt=attempt, question=question, answer=answer)
#             user_answer.save()

#         attempt.calculate_score()
#         messages.success(request, 'Exam submitted successfully.')
#         return redirect('exam_result', attempt_id=attempt.id)

#     return render(request, 'exam_attempt.html', {'exam': exam, 'questions': questions})


# def exam_result(request, attempt_id):
#     attempt = get_object_or_404(ExamAttempt, id=attempt_id)
#     return render(request, 'exam_result.html', {'attempt': attempt})
    