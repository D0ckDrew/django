from django.db import models
from django.contrib.auth.models import User

class Fish(models.Model):
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=200)
    rarity = models.IntegerField()

    def __str__(self):
        return self.name

class Fishing(models.Model):
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return self.user.__str__() + self.fish.name + self.weight
