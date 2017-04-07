from __future__ import unicode_literals

from django.db import models

class ImageAtQiniu(models.Model):
    fullname = models.CharField(max_length=120,unique=True)
    
    def __unicode__(self):
        return self.fullname

