from django.db import models

from django.utils import timezone

# Create your models here.

class QuestionList(models.Model):
    qid = models.AutoField(primary_key=True)
    Concept = models.CharField(max_length=100)
    Sub_concept1 = models.CharField(max_length=100, null=True)  # sub_concept 1 can be null
    Sub_concept2 = models.CharField(max_length=100, null=True)  # sub_concept 2 can be null
    Example = models.CharField(max_length=100)
    Meaning = models.CharField(max_length=100)
    Translation = models.CharField(max_length=100)


class WrongList(models.Model):
    uid = models.AutoField(primary_key=True)  # user id must be unique
    qid = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)  # keep updated
    cnt = models.CharField(max_length=100, null=True)  # error times can be null
