from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Clave", max_length=200, unique=True)
    name = models.CharField(verbose_name="red social", max_length=100)
    url = models.URLField(verbose_name="link", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Últ. fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name