from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Link
from .serializers import LinkSerializer


class LinkAPIViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

