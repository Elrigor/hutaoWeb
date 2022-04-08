from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return "Categoría: " + self.name        
            
class Command(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    categoria= models.ForeignKey(
            Categoria,
            on_delete=models.CASCADE,
            blank=True,
            null=True,
        )

    def __str__(self):
        return "Comando: " + self.name        

