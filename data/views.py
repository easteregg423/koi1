from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from data.models import Data


class DataView(ListView):
    model=Data
# Create your views here.
    def head(self, *args, **kwargs):
        last_data = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_data.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response