from django.db import models

class States(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

