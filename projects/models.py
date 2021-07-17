from django.db import models
from django.conf import settings
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage
from utils.uploadprojectimg import upload_project_img

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.TextField()
    link = models.URLField()
    image = ImageField(
        upload_to=upload_project_img,
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        blank=True,
        null=True
    )
    details = models.TextField()

    def __str__(self) -> str:
        return self.name