from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", unique=True, max_length=100)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name
