from django.db import models

app_label = 'Task'


class Task(models.Model):
    name = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)



