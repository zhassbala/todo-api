from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'\'{self.title}\', completed: {self.completed}'
