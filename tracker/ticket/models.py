from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    schedule_date = models.DateField()
    closed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
