from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="portfolio/images/thumbnail/")
    cover = models.ImageField(upload_to="portfolio/images/cover/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=1)
    created_at = models.DateField()

    def __str__(self):
        return self.title