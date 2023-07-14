import os
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    category_description = models.CharField(max_length=100,blank=True)
    category_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = "Categories"

    
class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_description = models.CharField(max_length=100,blank=True)
    course_image = models.ImageField(upload_to='course_images', blank=True, default='courses.gif')
    course_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.course_name
    
    def delete(self, *args, **kwargs):
        # Delete the course image file if it exists
        self.course_image.delete(save=False)
        
        super().delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        if self.id:
            old_instance = Course.objects.get(id=self.id)
            if self.course_image != old_instance.course_image:
                old_instance.course_image.delete(save=False)
        
        # Set the filename of the course_image to the course_name
        filename = f"{self.course_name}{os.path.splitext(self.course_image.name)[1]}"
        self.course_image.name = filename
        super().save(*args, **kwargs)
    
    
    
    class Meta:
        managed = True
        db_table = 'course'


class Exam(models.Model):
    exam_name = models.CharField(max_length=100, unique=True)
    exam_description = models.CharField(max_length=100,blank=True)
    exam_start_date = models.DateTimeField(blank=True)
    exam_duration = models.IntegerField(blank=True)
    exam_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.exam_name
    
    class Meta:
        managed = True
        db_table = 'exam'

class Question(models.Model):
    question_name = models.CharField(max_length=100, unique=True)
    question_text = models.CharField(max_length=200,blank=True)
    option1 = models.CharField(max_length=100,blank=True)
    option2 = models.CharField(max_length=100,blank=True)
    option3 = models.CharField(max_length=100,blank=True)
    option4 = models.CharField(max_length=100,blank=True)
    correct_answer = models.CharField(max_length=100,blank=True)
    question_status = models.BooleanField(default=True)
    question_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_name
    
    class Meta:
        managed = True
        db_table = 'question'



class Users(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'users'

# class ExamAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     score = models.IntegerField(blank=True, null=True)
#     start_time = models.DateTimeField(auto_now_add=True)
#     end_time = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return f"User: {self.user.username}, Exam: {self.exam.exam_name}"

#     def calculate_score(self):
#         correct_answers = 0
#         total_questions = self.exam.question_set.count()

#         for question in self.exam.question_set.all():
#             user_answer = self.useranswer_set.filter(question=question).first()
#             if user_answer and user_answer.answer == question.correct_answer:
#                 correct_answers += 1

#         self.score = (correct_answers / total_questions) * 100
#         self.save()

#     class Meta:
#         managed = True
#         db_table = 'exam_attempt'

class ExamAttempt(models.Model):
    session_id = models.CharField(max_length=32)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Session ID: {self.session_id}, Exam: {self.exam.exam_name}"

    def calculate_score(self):
        correct_answers = 0
        total_questions = self.exam.question_set.count()

        for question in self.exam.question_set.all():
            user_answer = self.useranswer_set.filter(question=question).first()
            if user_answer and user_answer.answer == question.correct_answer:
                correct_answers += 1

        self.score = (correct_answers / total_questions) * 100
        self.save()

    class Meta:
        managed = True
        db_table = 'exam_attempt'


class UserAnswer(models.Model):
    exam_attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Exam Attempt: {self.exam_attempt.id}, Question: {self.question.question_name}"

    class Meta:
        managed = True
        db_table = 'user_answer'


class ExamResult(models.Model):
    exam_attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    status_eye_tracking = models.BooleanField(default=False)
    status_mobile_detection = models.BooleanField(default=False)
    status_person_missing = models.BooleanField(default=False)
    status_second_person = models.BooleanField(default=False)
    image = models.ImageField(upload_to='exam_results/', null=True, blank=True)