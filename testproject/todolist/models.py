from django.db import models

# Create your models here.
class todolist(models.Model):
    task = models.CharField(max_length=20)
    flag = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task + " " + str(self.flag)