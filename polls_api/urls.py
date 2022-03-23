from django.urls import path
from .views import ListCreatePollView, DetailCreatePollView, Result, GeneralResult
urlpatterns = [
    path('polls/', ListCreatePollView.as_view()),
    path('polls/<int:pk>', DetailCreatePollView.as_view()),
    path('polls/candidate/<int:candidate_id>', Result.as_view()),
    path('polls/result/', GeneralResult.as_view()),
]