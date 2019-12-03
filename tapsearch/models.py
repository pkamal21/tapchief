from django.db import models

# Create your models here.
class TextSearch(models.Model):
    text = models.TextField(default="SOme")
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word