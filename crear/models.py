from django.db import models

# Create your models here.
class Tarea(models.Model):
    ESTADO_CHOICES = [('finalizada','Finalizada'),('incompleta','Incompleta')]
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=200)
    estado = models.CharField(max_length=50,choices=ESTADO_CHOICES,default='incompleta')
    def __str__(self):
        return self.titulo