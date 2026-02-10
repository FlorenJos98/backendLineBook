from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Autor, Libro
from .serializers import autorSerializer, libroSerializer

class AutorViewSet(viewsets.ModelViewSet):

    queryset = Autor.objects.all()
    serializer_class = autorSerializer
  
    @action(detail=True, methods=['post'],url_path='agregar_libro') #api/agregar_libro/
    def agregar_libro(self, request, pk=None):
        autor = self.get_object()
        serializer = libroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        libro = Libro.objects.create(
        
            titulo=serializer.validated_data['titulo'],
            isbn=serializer.validated_data['isbn'],
            fecha_publicacion=serializer.validated_data.get('fecha_publicacion'),
            autor=autor)
        
        return Response(libroSerializer(libro).data, status=status.HTTP_201_CREATED)

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = libroSerializer