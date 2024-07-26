from django.db import models

class ProgLang(models.Model):
    description = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.description