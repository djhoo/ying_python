from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets


# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
