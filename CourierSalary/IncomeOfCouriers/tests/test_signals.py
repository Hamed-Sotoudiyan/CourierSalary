import datetime

from django.test import TestCase

from IncomeOfCouriers.factories import TripFactory, CourierIncomeChangeFactory, UserFactory, CourierProfileFactory, \
    CourierDailySalaryFactory
from IncomeOfCouriers.models import CourierDailySalary, CourierWeeklySalary


class TestUpdateCourierDailySalary(TestCase):
    def setUp(self) -> None:
        self.date = datetime.date(2023, 5, 24)
        self.user = UserFactory()
        self.courier_profile = CourierProfileFactory(user=self.user)

        TripFactory(date=self.date, income=10000, courier=self.courier_profile)
        CourierIncomeChangeFactory(date=self.date, amount=4000, courier=self.courier_profile)
        CourierIncomeChangeFactory(date=self.date, amount=-2000, courier=self.courier_profile)

    def test_update_courier_daily_salary_in_specific_date(self):
        """
        When : courier_profile has one trip, and two courier_income_change =>  10000+4000-2000
        Then : Expected 12000 as daily salary saved CourierDailySalary for courier_profile at self.date
        """
        courier_daily_salary = CourierDailySalary.objects.get(courier=self.courier_profile, date=self.date)

        expected_daily_salary = 12000

        self.assertEqual(courier_daily_salary.daily_salary, expected_daily_salary)

    def test_update_courier_daily_salary_in_different_date(self):
        """
        When : create a Trip at another day.
        Then : Expected 12000 as daily salary saved CourierDailySalary for courier_profile.
        """
        TripFactory(date=datetime.date(2023, 5, 25), income=10000, courier=self.courier_profile)
        courier_daily_salary = CourierDailySalary.objects.get(courier=self.courier_profile,
                                                              date=self.date)

        expected_daily_salary = 12000

        self.assertEqual(courier_daily_salary.daily_salary, expected_daily_salary)


class TestUpdateCourierWeeklySalary(TestCase):
    def setUp(self) -> None:
        self.date = datetime.date(2023, 5, 24)
        self.user = UserFactory()
        self.courier_profile = CourierProfileFactory(user=self.user)

        CourierDailySalaryFactory(date=datetime.date(2023, 5, 20),
                                  daily_salary=10000,
                                  courier=self.courier_profile)
        CourierDailySalaryFactory(date=datetime.date(2023, 5, 21),
                                  daily_salary=15000,
                                  courier=self.courier_profile)
        CourierDailySalaryFactory(date=datetime.date(2023, 5, 24),
                                  daily_salary=7000,
                                  courier=self.courier_profile)
        CourierDailySalaryFactory(date=datetime.date(2023, 5, 18),
                                  daily_salary=11000,
                                  courier=self.courier_profile)

    def test_ensure_update_courier_weekly_salary(self):
        """
        When : courier_profile has 4 different daily-salary.
        Then : that must be saved in two different saturday.
                Saturday 2023-05-20 => 32000,
                Saturday 2023-05-13 => 11000.
        """

        courier_weekly_salary = CourierWeeklySalary.objects.get(courier=self.courier_profile,
                                                                week_starting_date=datetime.date(2023, 5, 20))
        expected_weekly_salary = 32000

        self.assertEqual(courier_weekly_salary.weekly_salary, expected_weekly_salary)
