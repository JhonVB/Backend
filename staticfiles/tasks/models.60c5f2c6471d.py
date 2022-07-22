from django.db import models

# Create your models here.

class Persona(models.Model):
   id = models.BigAutoField(primary_key=True)
   type_document= models.CharField(max_length=25)
   document= models.CharField(max_length=25, unique=True)
   name=models.CharField(max_length=25)
   last_name=models.CharField(max_length=35)
   hobbie=models.CharField(max_length=25)
   
   def __str__(self):
      return self.name