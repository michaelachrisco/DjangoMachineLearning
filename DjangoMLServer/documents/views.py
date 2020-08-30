from django.shortcuts import render
from documents.models import Document
from documents.serializers import DocumentSerializer
from rest_framework import viewsets


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
