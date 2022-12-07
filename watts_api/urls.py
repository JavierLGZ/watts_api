from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from watts_api import views

urlpatterns = [
    path("total_consume/", views.WattConsumeList.as_view()),
    path("daily_consume/", views.DailyWattConsume.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)