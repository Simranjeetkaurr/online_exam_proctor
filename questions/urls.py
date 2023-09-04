from django.urls import path
from .views import *

urlpatterns = [
    # creation of items
    path("courses", courses, name="courses"),
    path("exams", exams, name="exams"),
    path("questions", questions, name="questions"),
    # details and updation of items
    path("course/<int:courseid>", course_detail, name="course_detail"),
    path("exam/<int:exam_id>", exam_detail, name="exam_detail"),
    path("question/<int:question_id>", question_detail_edit, name="question_detail"),
    # deletion of items
    path("question/<int:question_id>/delete", delete_question, name="delete_question"),
    path("exam/<int:exam_id>/delete", exam_delete, name="delete_exam"),
#     # =====
#     path('your_view/', your_view, name='your_view'),
#     path('get_courses/<int:program_type>/', get_courses, name='get_courses'),
]