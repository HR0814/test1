from django.db import models

# Create your models here.
class 상식(models.Model):
    고유번호 = models.IntegerField()
    문제 = models.CharField(max_length=255)
    정답 = models.CharField(max_length=255)
    제한시간 = models.IntegerField()
    카테고리 = models.CharField(max_length=255)

    class Meta:
        db_table = '상식'
        app_label = 'secondapp'
        ordering = ['id']
        managed = False

    def __str__(self):
        return '@@@' + self.name

class 영화(models.Model):
    문제 = models.CharField(max_length=255)
    정답 = models.CharField(max_length=255)
    
    class Meta:
        db_table = '영화'
        app_label = 'secondapp'
        ordering = ['id']
        managed = False

    def __str__(self):
        return '@@@' + self.name

class words(models.Model):
    quiz = models.TextField()
    answer = models.TextField()
    hint = models.TextField()

    class Meta:
        db_table = '단어'
        app_label = 'secondapp'
        ordering = ['id']
        managed = False

    def __str__(self):
        return self.answer

class Music(models.Model):
    quiz = models.TextField()
    answer = models.TextField()
    link = models.TextField()
    info = models.TextField()
    hint = models.TextField()

    class Meta:
        db_table = '음악'
        app_label = 'secondapp'
        ordering = ['id']
        managed = False

    def __str__(self):
        return self.info

class Movie(models.Model):
    quiz = models.TextField()
    answer = models.TextField()
    info = models.TextField()
    hint = models.TextField()

    class Meta:
        db_table = '영화'
        app_label = 'secondapp'
        ordering = ['id']
        managed = False

    def __str__(self):
        return self.answer