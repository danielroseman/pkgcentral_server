from django.db import models

# Create your models here.

class Os(models.Model):
    name = models.CharField(max_length=100)
    code_name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    architecture = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s (%s) %s %s' % (self.name, self.code_name, self.version,
                                   self.architecture)


class Host(models.Model):
    name = models.CharField(max_length=100)
    seen = models.DateTimeField(blank=True, null=True)
    os = models.ForeignKey(Os, blank=True)
    comment = models.TextField(blank=True)
    packages = models.ManyToManyField('Package', blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.os.code_name)


class Group(models.Model):
    name = models.CharField(max_length=100)
    hosts = models.ManyToManyField(Host, blank=True)
    comment = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['name', 'version']

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.version)
