from django.urls import path
from .views import CandidateAPIView, CandidateDetails
urlpatterns = [
    path('candidate/', CandidateAPIView.as_view()),
    path('candidate-detail/<int:id>/', CandidateDetails.as_view()),
]
