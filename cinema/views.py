from .serializers import ActorSerializer, MovieSerializer
from rest_framework import generics
from .models import Actor, Movie

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



    
