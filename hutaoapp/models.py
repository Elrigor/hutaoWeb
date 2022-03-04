from django.db import models

class Commands(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()

def __str__(self):
        return "Comando: " + self.name