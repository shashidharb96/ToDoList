from django.db import models
from django.urls import reverse



class table_ToDo(models.Model):
    title=models.CharField(max_length=50)
    data=models.CharField(max_length=500)
    

    def __str__(self):
        return self.title

   # def get_absolute_url(self):
    #    return reverse('home')
