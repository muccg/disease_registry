from django.db import models
from django.conf import settings

class Module(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.code)

class EmailTemplate(models.Model):
    TARGETS = (
        (1, 'New patient registered'),
    )
    
    name = models.CharField(max_length=50)
    target = models.IntegerField(choices = TARGETS)
    description = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    
    def __unicode__(self):
        return '%s' % (self.name)