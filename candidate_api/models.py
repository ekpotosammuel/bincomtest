from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='images/', null=True)
    election_id = models.IntegerField()
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    experience = models.TextField(max_length=5000)
    gender = models.TextField(max_length=10)
    party = models.TextField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

