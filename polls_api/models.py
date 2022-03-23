from django.db import models


# Create your models here.
class Poll(models.Model):
    voter_id = models.IntegerField(unique=True)
    lga = models.CharField(max_length=100)
    party = models.TextField(max_length=10)
    candidate_id = models.IntegerField(unique=False)
    election_id = models.IntegerField(unique=False)

    def __int__(self):
        return self.voter_id

  