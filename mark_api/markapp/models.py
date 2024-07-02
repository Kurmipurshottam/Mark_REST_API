from django.db import models

# Create your models here.
class Marksheet(models.Model):
    subject=models.CharField(max_length=10)
    mark=models.IntegerField()
    performance=models.TextField()

    def __str__(self):
        return self.subject  + " || " +  self.performance