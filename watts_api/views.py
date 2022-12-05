from .models import WattConsume
from .serializers import WattSerializer

from rest_framework import generics, status


class WattConsumeList(generics.ListAPIView):
    serializer_class = WattSerializer
    queryset = WattConsume.objects.all()


