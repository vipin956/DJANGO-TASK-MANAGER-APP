from django.db import models

# Create your models here.
class TASK(models.Model):
    PRIORITY_CHOICES = [
        ('HIGH','HIGH'),
        ('MEDIUM','MEDIUM'),
        ('LOW','LOW'),
    ]

    STATUS_CHOICES = [
        ('PENDING','PENDING'),
        ('IN-PROGRESS','IN-PROGRESS'),
        ('COMPLETED','COMPLETED'),
    ]

    TITLE = models.CharField(max_length=150)
    DESCRIPTION = models.CharField(max_length=150)
    PRIORITY = models.CharField(max_length=200,choices=PRIORITY_CHOICES)
    STATUS = models.CharField(max_length=150,choices=STATUS_CHOICES)

    def __str__(self):
        return self.TITLE