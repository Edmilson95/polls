import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        # now - datimetime.timedelta(days=1) -> Verifica se self.pub_date (data de publicação) é maior ou igual à data de 24 horas atrás.
        # self.pub_date <= now -> Verifica se a data da publicacao é menor que a data/hora atual (não esta no futuro)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Cada Choice estsa relacionado a uma unica Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
