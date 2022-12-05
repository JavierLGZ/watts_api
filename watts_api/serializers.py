from rest_framework import serializers

from .models import WattConsume

class WattSerializer(serializers.ModelSerializer):
    class Meta:
        model = WattConsume
        fields =(
            "active_energy",
            "meter_date",
            "meter_id"
        )