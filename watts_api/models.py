from django.db import models

# Create your models here.
class WattConsume(models.Model):
    active_energy = models.FloatField()
    meter_date = models.DateTimeField()
    meter_id = models.IntegerField(unique=True)

    class Meta:
        ordering = ("meter_date",)
    
    def __str__(self) -> str:
        return str(self.meter_id)
    

