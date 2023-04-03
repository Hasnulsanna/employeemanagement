from django.db import models
    
class Expenses(models.Model):
    name = models.CharField(max_length=30, unique=True)
    amount= models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
	    return self.name
        
