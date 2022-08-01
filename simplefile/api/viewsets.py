from rest_framework import viewsets
from simplefile.models import (SimpleFile, SimpleFileCustom,
                               SimpleUploadValidation, SimpleFileDetails, SimpleFileId)
from .serializers import (SimpleFileSerializers, SimpleFileCustomSerializers,
                          SimpleFileValidationSerializers, SimpleFileDetailsSerializers,
                          SimpleFileIdSerializers)
from rest_framework import generics, mixins
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from rest_framework.pagination import PageNumberPagination


class SimpleFileViewSet(viewsets.ModelViewSet):
    queryset = SimpleFile.objects.all()
    serializer_class = SimpleFileSerializers


class SimpleFileCustomViewSet(viewsets.ModelViewSet):
    queryset = SimpleFileCustom.objects.all()
    serializer_class = SimpleFileCustomSerializers


class SimpleUploadValidationViewSet(viewsets.ModelViewSet):
    queryset = SimpleUploadValidation.objects.all().order_by('-id')
    serializer_class = SimpleFileValidationSerializers

    parser_classes = [MultiPartParser, FileUploadParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()


class SimpleUploadDetailsViewSet(viewsets.ModelViewSet):
    queryset = SimpleFileDetails.objects.all().order_by('-id')
    serializer_class = SimpleFileDetailsSerializers

    parser_classes = [MultiPartParser, FileUploadParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()


class SimpleUploadIdViewSet(viewsets.ModelViewSet):
    queryset = SimpleFileId.objects.all().order_by('-id')
    serializer_class = SimpleFileIdSerializers

    parser_classes = [MultiPartParser, FileUploadParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()
