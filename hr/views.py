from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from hr.models import doc
from hr.permissions import IsSuperUserOrHasGroupPermission
from hr.serializers import DocSerializer


class DocViewSet(ModelViewSet):
    permission_classes = [IsSuperUserOrHasGroupPermission,]
    serializer_class = DocSerializer
    queryset= doc.objects.all()
