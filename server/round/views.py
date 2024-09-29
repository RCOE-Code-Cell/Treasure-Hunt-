from rest_framework import generics
from .models import Groups
from .serializers import (
    TotalGroupsSerializer, Round1SelectedSerializer, Round1EliminatedSerializer,
    Round2SelectedSerializer, Round2EliminatedSerializer,
    Round3SelectedSerializer, Round3EliminatedSerializer,
    Round4SelectedSerializer, Round4EliminatedSerializer,
    WinnerSerializer
)

class TotalGroupsView(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = TotalGroupsSerializer

class Round1SelectedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round1=True)
    serializer_class = Round1SelectedSerializer

class Round1EliminatedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round1=False)
    serializer_class = Round1EliminatedSerializer

class Round2SelectedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round2=True)
    serializer_class = Round2SelectedSerializer

class Round2EliminatedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round2=False)
    serializer_class = Round2EliminatedSerializer

class Round3SelectedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round3=True)
    serializer_class = Round3SelectedSerializer

class Round3EliminatedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round3=False)
    serializer_class = Round3EliminatedSerializer

class Round4SelectedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round4=True)
    serializer_class = Round4SelectedSerializer

class Round4EliminatedView(generics.ListAPIView):
    queryset = Groups.objects.filter(round4=False)
    serializer_class = Round4EliminatedSerializer

class Round2TotalGroupsView(generics.ListAPIView):
    queryset = Groups.objects.filter(round1=True)
    serializer_class = Round2SelectedSerializer

class Round3TotalGroupsView(generics.ListAPIView):
    queryset = Groups.objects.filter(round2=True)
    serializer_class = Round3SelectedSerializer

class Round4TotalGroupsView(generics.ListAPIView):
    queryset = Groups.objects.filter(round3=True)
    serializer_class = Round4SelectedSerializer


class WinnerView(generics.ListAPIView):
    queryset = Groups.objects.filter(winner=True)
    serializer_class = WinnerSerializer
