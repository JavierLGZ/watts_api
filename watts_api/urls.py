from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from watts_api import views

app_name = "watts_api"

urlpatterns = [
    path("", views.DailyWattConsume.as_view(), name="wattsdetail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
