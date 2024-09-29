from django.urls import path
from .views import (
    TotalGroupsView, Round1SelectedView, Round1EliminatedView,
    Round2SelectedView, Round2EliminatedView,
    Round3SelectedView, Round3EliminatedView,
    Round4SelectedView, Round4EliminatedView,
    WinnerView, Round2TotalGroupsView, Round3TotalGroupsView, Round4TotalGroupsView
)

urlpatterns = [
    path('total-groups/', TotalGroupsView.as_view(), name='total-groups'),
    path('round1-selected/', Round1SelectedView.as_view(), name='round1-selected'),
    path('round1-eliminated/', Round1EliminatedView.as_view(), name='round1-eliminated'),
    path('round2-selected/', Round2SelectedView.as_view(), name='round2-selected'),
    path('round2-eliminated/', Round2EliminatedView.as_view(), name='round2-eliminated'),
    path('round3-selected/', Round3SelectedView.as_view(), name='round3-selected'),
    path('round3-eliminated/', Round3EliminatedView.as_view(), name='round3-eliminated'),
    path('round4-selected/', Round4SelectedView.as_view(), name='round4-selected'),
    path('round4-eliminated/', Round4EliminatedView.as_view(), name='round4-eliminated'),
    path('round2-total/', Round2TotalGroupsView.as_view(), name='round2-total'),
    path('round3-total/', Round3TotalGroupsView.as_view(), name='round3-total'),
    path('round4-total/', Round4TotalGroupsView.as_view(), name='round4-total'),
    path('winner/', WinnerView.as_view(), name='winner'),
]
