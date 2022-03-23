from django.urls import path
from .views import ElectionAPIView, ElectionDetails, TypeAPIView, TypeDetails

urlpatterns = [
    path('election/', ElectionAPIView.as_view()),
    path('election/<int:id>/', ElectionDetails.as_view()),
    path('election-type/', TypeAPIView.as_view()),
    path('election-type/<int:id>/', TypeDetails.as_view()),
]
