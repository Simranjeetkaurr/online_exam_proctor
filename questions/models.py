import os
from django.db import models



class Acourse(models.Model):
    courseid = models.AutoField(db_column='CourseId', primary_key=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='CourseCode', max_length=10)
    descriptions = models.CharField(db_column='Descriptions', max_length=250, blank=True, null=True)
    bannerimagename = models.CharField(db_column='BannerImageName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coursesession = models.IntegerField(db_column='CourseSession') # Field name made lowercase.
    programtype = models.IntegerField(db_column='ProgramType')
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')
    semester = models.IntegerField(db_column='Semester')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ACourse'
        
        
class Configuration(models.Model):
    configurationid = models.AutoField(db_column='ConfigurationId', primary_key=True) 
    moduleid = models.IntegerField(db_column='ModuleId')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isactivesession = models.BooleanField(db_column='IsActiveSession')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Configuration'

class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=100, unique=True)
    exam_description = models.CharField(max_length=100,blank=True)
    exam_start_date = models.DateTimeField(blank=True)
    exam_duration = models.IntegerField(blank=True)
    exam_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    courseid = models.ForeignKey(Acourse,on_delete=models.DO_NOTHING)  # Field name made lowercase.

    def __str__(self):
        return self.exam_name

    class Meta:
        managed = False
        db_table = 'exam'


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_name = models.TextField(max)
    question_text = models.TextField(max)
    question_image = models.TextField(max)
    option1 = models.TextField(max)
    option2 = models.TextField(max)
    option3 = models.TextField(max)
    option4 = models.TextField(max)
    correct_answer = models.TextField(max)
    question_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    userid = models.CharField(db_column='UserId',max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    descriptions = models.CharField(db_column='Descriptions', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastmodifiedon = models.DateTimeField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
    firstenteredby = models.CharField(db_column='FirstEnteredBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstenteredon = models.DateTimeField(db_column='FirstEnteredOn', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.question_name

    class Meta:
        managed = True
        db_table = 'question'
        
