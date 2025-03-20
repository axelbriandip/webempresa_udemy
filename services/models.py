from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name="título")
    subtitle =  models.CharField(max_length=100, verbose_name="subtítulo")
    description =  models.TextField(max_length=200, verbose_name="descripción")
    image = models.ImageField(verbose_name="imágen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title