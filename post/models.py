from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField



class MyModel(models.Model):
    description = RichTextField()

