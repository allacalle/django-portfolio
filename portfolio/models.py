from django.db import models




class Project (models.Model):
    title = models.CharField(_(""), max_length=100)
    description = models.CharField(_(""), max_length=250)
    image = models.ImageField(_(""), upload_to='portfolio/images', height_field=None, width_field=None, max_length=None)
    url = models.URLField(_(""), max_length=200, blank=True)
    
