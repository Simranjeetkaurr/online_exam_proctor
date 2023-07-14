from django.urls import path
from .views import *

urlpatterns = [
    # creation of items
    path("courses", courses, name="courses"),
    path("exams", exams, name="exams"),
    path("questions", questions, name="questions"),
    # details and updation of items
    path("category/<int:category_id>", category_detail, name="category_detail"),
    path("course/<int:course_id>", course_detail, name="course_detail"),
    path("exam/<int:exam_id>", exam_detail, name="exam_detail"),
    path("question/<int:question_id>", question_detail_edit, name="question_detail"),
    # deletion of items
    path("question/<int:question_id>/delete", delete_question, name="delete_question"),
    path("course/<int:course_id>/delete", course_delete, name="delete_course"),
    path("exam/<int:exam_id>/delete", exam_delete, name="delete_exam"),
    path("category/<int:category_id>/delete", category_delete, name="delete_category"),

    path("exam/<int:exam_id>/attempt", exam_attempt, name="exam_attempt"),
    path('exam/result/<int:attempt_id>/',exam_result, name='exam_result'),
    path('question_popup/', question_popup, name='question_popup'),
    # path('exam_attempt/<int:exam_id>/', exam_attempt, name='exam_attempt'),
    
]
