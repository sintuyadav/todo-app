from django.db import models

# Create your models here.
class Mytodo(models.Model):
    task = models.CharField(max_length=50)
    status = models.CharField(max_length=50 ,default='incomplete')
    def __str__(self) :
        return self.task

        