from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [('todo','TODO'),('inprogress','INPROGRESS'),('completed','COMPLETED')]
    PRIORITY_CHOICES = [('high','HIGH'),('low','LOW'),('medium','MEDIUM')]
    title = models.CharField()
    description = models.TextField()
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='task_task_assigned_to')
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default='todo')
    priority = models.CharField(max_length=20,choices = PRIORITY_CHOICES,default='low')
    duedate = models.DateField(null=True, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.title
