from rest_framework import serializers
from .models import Autor, Libro

class libroSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(read_only= True)

    class Meta:
        model = Libro
        fields = ['id' , 'titulo' , 'isbn', 'fecha_publicacion', 'autor' ]

    def validate_isbn (self, value):
        if len(value) < 5:
            raise serializers.ValidationError('El isbn debe tener almenos 5 caracteres')
        return value
    
class autorSerializer(serializers.ModelSerializer):
    libros = libroSerializer(many = True, read_only = True)

    class Meta:
        model = Autor
        fields = ['id' , 'nombre' , 'pais', 'fecha_nacimiento', 'libros' ]