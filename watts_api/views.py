from .models import WattConsume
from .serializers import WattSerializer, OutputSerializer
from datetime import datetime, timedelta
import calendar

from rest_framework import generics
from rest_framework.response import Response



def daily_consume(td):
    return_data = []
    for i in range(24):
        consume_last = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=td.day,
            meter_date__hour=i
        ).last()
        consume_first = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=td.day,
            meter_date__hour=i
        ).first()
        td_hour = td + timedelta(hours=i)
        active_energy_last = consume_last.active_energy if consume_last is not None else 0
        active_energy_first = consume_first.active_energy if consume_first is not None else 0
        total_consume = active_energy_last - active_energy_first
        hour_consume = {
                "meter_date": td_hour.isoformat(" ","seconds"),
                "value": total_consume
        }
        return_data.append(hour_consume)
    return return_data

def weekly_consume(td):
    return_data = []
    week_day = td.weekday()
    for i in range(7):
        consume_last = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=td.day - week_day + i
        ).last()
        consume_first = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=td.day - week_day + i
        ).first()
        td_hour = td + timedelta(days=i-week_day)
        active_energy_last = consume_last.active_energy if consume_last is not None else 0
        active_energy_first = consume_first.active_energy if consume_first is not None else 0
        total_consume = active_energy_last - active_energy_first
        hour_consume = {
                "meter_date": td_hour.isoformat(" ","seconds"),
                "value": total_consume
        }
        return_data.append(hour_consume)
    return return_data

def montly_consume(td):
    total_days = calendar.monthrange(td.year, td.month)
    return_data = []
    print(total_days)
    for i in range(1, total_days[-1] + 1):
        consume_last = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=i
        ).last()
        consume_first = WattConsume.objects.filter(
            meter_date__year=td.year,
            meter_date__month=td.month,
            meter_date__day=i
        ).first()
        td_hour = td.replace(day=i)
        active_energy_last = consume_last.active_energy if consume_last is not None else 0
        active_energy_first = consume_first.active_energy if consume_first is not None else 0
        total_consume = active_energy_last - active_energy_first
        hour_consume = {
                "meter_date": td_hour.isoformat(" ","seconds"),
                "value": total_consume
        }
        return_data.append(hour_consume)
    return return_data


class WattConsumeList(generics.ListAPIView):
    serializer_class = WattSerializer
    queryset = WattConsume.objects.all()


class DailyWattConsume(generics.ListAPIView):
    serializer_class = OutputSerializer
    queryset = WattConsume.objects.all()

    def get(self, request, *args, **kwargs):
        date_param = self.request.query_params.get("date", None)
        period_param = self.request.query_params.get("period", None)
        print(date_param, period_param)
        td = datetime.strptime(date_param, "%Y-%m-%d")
        print()
        return Response(montly_consume(td=td))








