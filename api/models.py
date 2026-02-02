from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __srt__ (self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20 , unique=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE, related_name='libros')

    def __srt__ (self):
        return self.titulo
    