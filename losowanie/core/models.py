from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=25)
    voted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}, {self.voted}"

class Scope(models.Model):
    name = models.CharField(max_length=25)
    isChosen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}, {self.isChosen}"

class Voter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    chosen_person = models.ForeignKey(Scope, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.email}, {self.ip_address}"
    


