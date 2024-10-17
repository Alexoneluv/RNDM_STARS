from django.db import models

class UploadedFile(models.Model):
    ATMOSPHERE_CHOICES = [
        ('egyptian', 'Египетская'),
        ('jungle', 'Джунглей'),
        ('marine', 'Морская'),
        ('persian', 'Персидская'),
        ('japanese', 'Японская'),
        ('russian', 'Российская'),
    ]

    file = models.FileField(upload_to='uploads/')
    theme = models.CharField(max_length=50, default='Природа')
    atmosphere = models.CharField(max_length=50, choices=ATMOSPHERE_CHOICES)
    hashtags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.file.name