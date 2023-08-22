from django.urls import path
from .views import ActorListCreateView, MovieListCreateView

urlpatterns = [
    path('actor/', ActorListCreateView.as_view()),
    path('movie/', MovieListCreateView.as_view()),
    
]