from django.db import models

class Hobbies(models.Model):
    description = models.CharField(max_length=25)

    def __str__(self):
        return self.description


    