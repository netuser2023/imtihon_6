from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')
    

    def __str__(self) -> str:
        return self.first_name

class Matematic(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    answer = models.TextField()



    
