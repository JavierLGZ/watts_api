from datetime import datetime, timedelta

from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import WattConsume


class WattTests(APITestCase):
    fixture = ["fixture.json"]
    url = reverse("watts_api:wattsdetail")

    def setUp(self):
        call_command("loaddata", "fixture.json", verbosity=0)

    def test_view(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_daily_value(self):
        response = self.client.get("/?date=2022-10-12", format="json")
        self.assertEqual(
            response.data[0], {"meter_date": "2022-10-12 00:00:00", "value": 0}
        )
        self.assertEqual(len(response.data), 24)

    def test_weekly_value(self):
        day = "2022-10-20"
        period = "weekly"
        response = self.client.get(f"/?date={day}&period={period}", format="json")
        print(response.data)
        self.assertEqual(
            response.data[0],
            {"meter_date": "2022-10-17 00:00:00", "value": 490.44433000000026},
        )
        week_day = datetime.strptime(day, "%Y-%m-%d").weekday()
        monday = datetime.strptime(day, "%Y-%m-%d") - timedelta(days=week_day)
        response_monday = datetime.strptime(
            response.data[0]["meter_date"], "%Y-%m-%d %H:%M:%S"
        )
        self.assertEqual(len(response.data), 7)
        self.assertEqual(monday.day, response_monday.day)
