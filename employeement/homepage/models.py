from django.db import models
    

class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)

    def __str__(self):
        return self.name

