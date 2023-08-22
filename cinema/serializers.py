from rest_framework.serializers import ModelSerializer

from .models import Actor, Movie

class ActorSerializer(ModelSerializer):
  
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

