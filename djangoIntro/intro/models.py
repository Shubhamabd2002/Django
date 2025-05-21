from django.db import models
from django.utils import timezone
# Create your models here.
class introVerity(models.Model):
    INTRO_TYPE_CHOICE = [
        ('ML', "MASALA"),
        ('GR', "GINGER"),
        ('KL', "KIWI"),
        ('PL', "PLAIN"),
        ('EL', "ELAICHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='intro/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=INTRO_TYPE_CHOICE)

