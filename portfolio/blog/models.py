from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=20)
  publication_date = models.DateField(auto_now=True)
  para = models.TextField(max_length=1000)
  image =models.ImageField(upload_to='images/')
