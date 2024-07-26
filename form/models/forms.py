from django.db import models
from uploader.models import Image
from .hobbies import Hobbies
from .states import States
from .proglang import ProgLang

class Forms(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    perfil = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+', blank=True, null=True, default=None)
    biografia = models.TextField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    hobbies = models.ManyToManyField(Hobbies)
    states = models.ManyToManyField(States)
    programming = models.ManyToManyField(ProgLang)

    def __str__(self):
        return self.username