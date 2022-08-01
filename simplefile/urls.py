from django.urls import path, include
from rest_framework import routers
from .api.viewsets import (SimpleFileViewSet, SimpleFileCustomViewSet, SimpleUploadValidationViewSet,
                           SimpleUploadDetailsViewSet, SimpleUploadIdViewSet)

router = routers.DefaultRouter()
router.register('simples', SimpleFileViewSet)
router.register('custom', SimpleFileCustomViewSet)
router.register('validation', SimpleUploadValidationViewSet)
router.register('details', SimpleUploadDetailsViewSet)
router.register('ids', SimpleUploadIdViewSet)

urlpatterns = [
    path('', include(router.urls))
]
