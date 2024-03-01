from rest_framework.viewsets import ModelViewSet

from cinema.models import CinemaHall, Movie, Actor, MovieSession, Genre
from cinema.serializers import (
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    GenreSerializer,
    MovieSessionListSerializer,
)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = (
        Movie.objects
        .prefetch_related("genres", "actors")
    )
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return self.serializer_class


class MovieSessionViewSet(ModelViewSet):
    queryset = (
        MovieSession.objects
        .select_related("movie", "cinema_hall")
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return self.serializer_class
