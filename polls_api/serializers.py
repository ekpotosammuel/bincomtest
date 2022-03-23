from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'voter_id', 'candidate_id', 'election_id')

class PollResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        # fields = ('id', 'voter_id', 'candidate_id', 'election_id')