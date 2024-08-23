from django.db import models

# Create your models here.
class Novel(models.Model):
  title = models.CharField(max_length=150)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=50)
  description = models.TextField()
  published_date =models.DateField(blank=False)
  edition = models.IntegerField()
  bnanner = models.ImageField(default='fallback.webp',blank=True)
  