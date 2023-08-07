import os
from django.db import models
from questions.models import *
from django.contrib.sessions.models import Session



class Result(models.Model):
    id= models.AutoField(primary_key=True)
    django_session = models.CharField(max_length=100)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.TextField(max_length=200)
    given_answer= models.TextField(max_length=200,null=True)
    marks_obtained = models.IntegerField()
    attempt_date_time = models.DateTimeField(auto_now_add=True,blank=True)
    total_attempt= models.IntegerField()
    
    def __str__(self):
        return self.id
    
    class Meta:
        managed = True
        db_table = 'result'