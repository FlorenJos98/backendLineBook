from rest_framework import serializers
from .models import Autor, Libro
from django.contrib.auth.hashers import make_password


class libroSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(read_only= True)

    class Meta:
        model = Libro
        fields = ['id' , 'titulo' , 'isbn', 'fecha_publicacion', 'autor' ]
        '''extra_kwargs = {
            'contrasena': {'write_only': True}
        }'''

    def validate_isbn (self, value):
        if len(value) < 5:
            raise serializers.ValidationError('El isbn debe tener almenos 5 caracteres')
        return value
    
''' def validate_contrasena(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'La contraseña debe tener al menos 8 caracteres'
            )
        return value

    def create(self, validated_data):
        validated_data['contrasena'] = make_password(
            validated_data['contrasena']
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'contrasena' in validated_data:
            validated_data['contrasena'] = make_password(
                validated_data['contrasena']
            )
        return super().update(instance, validated_data)
'''
class autorSerializer(serializers.ModelSerializer):
    libros = libroSerializer(many = True, read_only = True)

    class Meta:
        model = Autor
        fields = ['id' , 'nombre' , 'pais', 'fecha_nacimiento', 'libros' ]