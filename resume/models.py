from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Experience(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    specialty = models.TextField()
    place = models.TextField()
    description = models.TextField()
    timedelta = models.TextField()

    def __str__(self) -> str:
        return self.place