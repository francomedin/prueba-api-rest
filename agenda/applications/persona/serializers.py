from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('__all__')

class PersonaSerializers(serializers.Serializer):
    id=serializers.IntegerField()
    full_name=serializers.CharField()
    job=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    #Este atributo no es necesario en el modelo Person tambien puede ser required=False
    activo=serializers.BooleanField(default=False)

class PersonSerializers2(serializers.ModelSerializer):
    #Aqui podemos agregar atributos que no vengan con el modelo
    activo=serializers.BooleanField(default=False)

    class Meta:
        model=Person
        fields=('__all__')


class ReunionSerializers(serializers.ModelSerializer):
    #Esto hace que la api muiestre el serializador de la persona
    persona=PersonSerializers()

    class Meta:
        model=Reunion
        fields=(
            'id',
            'fecha',
            'hora',
            'persona',
        )


class HobbySerializers(serializers.ModelSerializer):

    class Meta:
        model=Hobby
        fields=('__all__')


class PersonSerializers3(serializers.ModelSerializer):
    hobby=HobbySerializers(many=True)
    class Meta:
        model=Person
        fields=(
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobby',
            )


class ReunionSerializers2(serializers.ModelSerializer):

    fecha_hora=serializers.SerializerMethodField()

    class Meta:
        model=Reunion
        fields=(
            'id',
            'fecha',
            'hora',
            'persona',
            'fecha_hora'
        )
    
    def get_fecha_hora(self,obj):
        return str(obj.fecha) +', ' +  str(obj.hora)


class ReunionSerializersLink(serializers.HyperlinkedModelSerializer):


    class Meta:
        model=Reunion
        fields=(
            'id',
            'fecha',
            'hora',
            'persona',
        )
        extra_kwargs={
            'persona':{'view_name':'persona_app:detail-persona','lookup_field':'pk'}
        }
    
   
class PersonPagination(pagination.PageNumberPagination):
    page_size=2
    max_page_size=50

class PersonSerializers4(serializers.Serializer):
    persona__job=serializers.CharField()
    cantidad=serializers.IntegerField()

   