from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Person, Reunion
from .serializers import (
PersonSerializers,
 PersonaSerializers,
 PersonSerializers2,
 ReunionSerializers,
 PersonSerializers3,
 ReunionSerializers2,
 ReunionSerializersLink,
 PersonPagination,
 PersonSerializers4,
)
# Paquete DRF
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, #Equivalente a detail view
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

class ListaPersonas(ListView):
    template_name="persona/personas.html"
    context_object_name='personas'

    def get_queryset(self):
        return Person.objects.all()

class ListaApiViewPersona(ListAPIView):
    serializer_class=PersonSerializers

    def get_queryset(self):
        return Person.objects.all()


class BuscarPersona(TemplateView):
    template_name='persona/lista.html'


class PersonCreateView(CreateAPIView):
    serializer_class=PersonSerializers


class PersonRetrieveAPIView(RetrieveAPIView):

    serializer_class=PersonSerializers
    queryset=Person.objects.all()


class PersonDeleteView(DestroyAPIView):
    
    serializer_class=PersonSerializers
    queryset=Person.objects.all()

class PersonUpdateAPIView(UpdateAPIView):
    serializer_class=PersonSerializers
    queryset=Person.objects.all()

class PersonUpdateRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class=PersonSerializers
    queryset=Person.objects.all()


class PersonaListAPI2(ListAPIView):
    
    #serializer_class=PersonaSerializers
    serializer_class=PersonSerializers2
    def get_queryset(self):
        return Person.objects.all()


class ReunionAPIView(ListAPIView):
    serializer_class=ReunionSerializers2
    
    def get_queryset(self):
        return Reunion.objects.all()


class PersonaListAPI3(ListAPIView):
    
    #serializer_class=PersonaSerializers
    serializer_class=PersonSerializers3
    def get_queryset(self):
        return Person.objects.all()

        

class ReunionAPIViewLink(ListAPIView):
    serializer_class=ReunionSerializersLink
    
    def get_queryset(self):
        return Reunion.objects.all()

#Vista persona con apginacion
class PersonPaginationList(ListAPIView):
    serializer_class=PersonSerializers
    pagination_class=PersonPagination

    def get_queryset(self):
        return Person.objects.all()

class ReunionByJobs(ListAPIView):
    serializer_class=PersonSerializers4

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones()