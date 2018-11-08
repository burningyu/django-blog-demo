# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   ## A model in Django is a special kind of object – it is saved in the database.A model in the database is a spreadsheet with columns (fields) and rows (data)
    ## models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title