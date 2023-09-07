from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen", upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última edición")

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
    
    # Mostrar el título en el listado de proyectos  (en el admin)
    def __str__(self):
        return self.title