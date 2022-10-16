from django.db import models

# Create your models here.
class Link(models.Model):
    def __str__(self):
        return str(self.name)
    tag = models.CharField(max_length=1000, default="A")
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

class Img(models.Model):
    def __str__(self):
        return str(self.name)
    tag = models.CharField(max_length=1000, default="img")
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

class H1(models.Model):
    def __str__(self):
        return str(self.inner_text)
    tag = models.CharField(max_length=1000, default="h1")
    inner_text= models.CharField(max_length=1000, null=True, blank=True)
    class_name= models.CharField(max_length=1000, null=True, blank=True)

class H2(models.Model):
    def __str__(self):
        return str(self.inner_text)
    tag = models.CharField(max_length=1000, default="h2")
    inner_text= models.CharField(max_length=1000, null=True, blank=True)
    class_name= models.CharField(max_length=1000, null=True, blank=True)

class Paragraph(models.Model):
    def __str__(self):
        return str(self.inner_text)
    tag = models.CharField(max_length=1000, default="paragraph")
    inner_text= models.CharField(max_length=1000, null=True, blank=True)
    class_name= models.CharField(max_length=1000, null=True, blank=True)