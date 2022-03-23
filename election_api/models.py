from django.db import models

# Create your models here.

class Election(models.Model):
    name = models.CharField(max_length=150)
    election_type_id = models.IntegerField()
    year = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
