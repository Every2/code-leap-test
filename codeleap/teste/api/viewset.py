from rest_framework import viewsets, status
from teste.api import serializers
from teste import models
from rest_framework.response import Response

class DataStructureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DataStructureSerializer
    queryset = models.DataStructure.objects.all()

    http_method_names = ['get', 'post', 'delete', 'patch']

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        valid_fields = {'title', 'content'}
        field_in_request = set(request.data.keys())

        if not field_in_request.issubset(valid_fields):
            return Response({'error: Invalid fields provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        fields_to_update = {key: value for key, value in request.data.items() if key in valid_fields}

        serializer.is_valid(raise_exception=True)
        serializer.update(instance, fields_to_update)

        return Response(serializer.data)

    
