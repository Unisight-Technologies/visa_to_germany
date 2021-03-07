from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=400)
    message = models.CharField(max_length=800)


class News(models.Model):
    title = models.CharField(max_length=300)
    date = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=800)
    url = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
