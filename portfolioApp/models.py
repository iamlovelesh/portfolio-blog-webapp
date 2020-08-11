from django.db import models

# Create your models here.
class UserMessage(models.Model):
    Full_Name = models.CharField(max_length=254)
    # last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    message=models.TextField(max_length=550)

    def __str__(self):
        return self.Full_Name
