from django.shortcuts import render
from .models import Image, Video
from .serializers import ImageSerializer, VideoSerializer
from accounts.permissions import isAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [isAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        """
        add an image link to the gallery
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """
        Remove and image from the image gallery
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("image deleted", status=status.HTTP_204_NO_CONTENT)

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [isAdminOrReadOnly]


