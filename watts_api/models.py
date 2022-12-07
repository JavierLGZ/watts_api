from django.db import models

# Create your models here.
class WattConsume(models.Model):
    active_energy = models.FloatField()
    meter_date = models.DateTimeField()
    meter_id = models.IntegerField()

    class Meta:
        ordering = ("meter_date",)
    

