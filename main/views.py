from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet

from main.models import *
from .serializers import ProblemaSerializer

#
# class ProblemaListView(ListAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#
# class ProblemaDetailView(RetrieveAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#
# class ProblemaCreateView(CreateAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class ProblemaUpdateView(UpdateAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class ProblemaDeleteView(DestroyAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer


class ProblemaViewSet(ModelViewSet):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

    def get_serializer_context(self):
        return {'request': self.request}