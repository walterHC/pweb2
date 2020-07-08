from django.db import models

# Create your models here.

class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCiudad = models.CharField(max_length = 50) 
    imagenCiudad = models.ImageField(upload_to='pics')
    descripcionCiudad = models.TextField()
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)


    def get_absolute_url(self):
        return "/administration/" + str(self.id) +"/"
