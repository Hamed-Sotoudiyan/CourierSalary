from datetime import timedelta

from django.db import transaction
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Trip, CourierIncomeChange, CourierDailySalary, CourierWeeklySalary


@receiver(post_save, sender=Trip)
@receiver(post_save, sender=CourierIncomeChange)
@transaction.atomic
def update_courier_daily_salary(sender, instance, **kwargs):
    """
        signals from Trip and CourierIncomeChange to daily salary
    With every change in these 2 models, this function runs.

    according to increase or decrease in income, or change in trips on a particular day,
    The daily income is calculated for that day.
    """
    courier = instance.courier
    date = instance.date
    # Investigation on Trip
    trip_income_sum = Trip.objects.filter(courier=courier, date=date).aggregate(Sum('income'))['income__sum'] or 0
    # Investigation on CourierIncomeChange
    change_income_sum = CourierIncomeChange.objects.filter(courier=courier, date=date).aggregate(Sum('amount'))[
                            'amount__sum'] or 0
    total_income = trip_income_sum + change_income_sum
    # finding particular day (or creating) and updating daily salary
    courier_daily_salary, created = CourierDailySalary.objects.get_or_create(courier=courier, date=date)
    courier_daily_salary.daily_salary = total_income
    courier_daily_salary.save()


@receiver(post_save, sender=CourierDailySalary)
@transaction.atomic
def update_courier_weekly_salary(sender, instance, **kwargs):
    """
        signals from daily salary to weekly salary
    With every change in this model, this function runs.

    according to changes in daily salary on a particular week,
    The weekly income is calculated for that saturday.
    """
    courier = instance.courier
    date = instance.date
    weekday = date.weekday()
    # calculate the Monday of the current week
    week_start_date = date - timedelta(days=weekday)
    # get the Saturday of the current week
    saturday_date = week_start_date - timedelta(days=2) if weekday <= 4 else week_start_date + timedelta(days=5)
    # get the next Saturday
    next_saturday = saturday_date + timedelta(days=7)
    # Investigation on daily salary
    daily_salary_sum = \
        CourierDailySalary.objects.filter(courier=courier, date__range=[saturday_date, next_saturday]).aggregate(
            Sum('daily_salary'))['daily_salary__sum'] or 0

    # finding particular saturday (or creating) and updating weekly salary
    courier_weeklysalary, created = CourierWeeklySalary.objects.get_or_create(courier=courier,
                                                                              week_starting_date=saturday_date)
    courier_weeklysalary.weekly_salary = daily_salary_sum
    courier_weeklysalary.save()
