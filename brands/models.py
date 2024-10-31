from django.db import models

class Brand(models.Model):
    primary_color = models.CharField(max_length=100, blank=True, null=True)
    secondary_color = models.CharField(max_length=100, blank=True, null=True)
    # logo = models.ImageField(upload_to='brands/logos/', blank=True, null=True)
    # cover_image = models.ImageField(upload_to='brands/cover_images/', blank=True, null=True)


