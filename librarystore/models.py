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


#relationships
class Person(models.Model):
  name = models.CharField(max_length=128)

  def __str__(self):
    return self.name

class Group(models.Model):
  name = models.CharField(max_length=128)
  members = models.ManyToManyField(Person, through='Membership')

  def __str__(self):
    return self.name
  
class Membership(models.Model):
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  date_joined = models.DateField()
  invite_reason = models.CharField(max_length=64)
  
  def __str__(self):
    return f"{self.person} {self.date_joined} {self.invite_reason}"