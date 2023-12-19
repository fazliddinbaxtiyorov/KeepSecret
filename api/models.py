from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='like')
    comment = models.IntegerField(default=0)
    hashtag = models.CharField(max_length=255)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quests_text = models.ForeignKey(Question, on_delete=models.PROTECT, db_constraint=True)
    answer_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


