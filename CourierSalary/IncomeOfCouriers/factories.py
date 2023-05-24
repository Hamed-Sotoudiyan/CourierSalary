import datetime

import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone
from factory.fuzzy import FuzzyFloat, FuzzyInteger, FuzzyDate

from .models import CourierProfile, Trip, CourierIncomeChange, CourierDailySalary, CourierWeeklySalary


class UserFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    is_staff = True
    is_superuser = True

    class Meta:
        model = User


class CourierProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    phone_number = '09121111111'
    address = 'خیابان - کوچه - پلاک'

    class Meta:
        model = CourierProfile


class TripFactory(factory.django.DjangoModelFactory):
    distance = FuzzyFloat(0, 900)
    date = FuzzyDate(datetime.date(2008, 1, 1))
    distance_from_origin = FuzzyFloat(0, 900)
    time_of_day = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    income = FuzzyInteger(0, 10000)
    courier = factory.SubFactory(CourierProfileFactory)

    class Meta:
        model = Trip


class CourierIncomeChangeFactory(factory.django.DjangoModelFactory):
    courier = factory.SubFactory(CourierProfileFactory)
    amount = FuzzyFloat(0, 900)
    date = FuzzyDate(datetime.date(2008, 1, 1))

    class Meta:
        model = CourierIncomeChange


class CourierDailySalaryFactory(factory.django.DjangoModelFactory):
    courier = factory.SubFactory(CourierProfileFactory)
    date = FuzzyDate(datetime.date(2008, 1, 1))
    daily_salary = FuzzyFloat(0, 900)

    class Meta:
        model = CourierDailySalary


class CourierWeeklySalaryFactory(factory.django.DjangoModelFactory):
    courier = factory.SubFactory(CourierProfileFactory)
    week_starting_date = FuzzyDate(datetime.date(2008, 1, 1))
    weekly_salary = FuzzyFloat(0, 900)

    class Meta:
        model = CourierWeeklySalary
