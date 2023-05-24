from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class CourierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    address = models.CharField(max_length=200, verbose_name='آدرس')

    # add other attributes of courier

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'پیک'
        verbose_name_plural = 'پیک ها'


class Trip(models.Model):
    courier = models.ForeignKey(CourierProfile, on_delete=models.CASCADE)

    distance = models.FloatField(verbose_name='مسافت')
    customer_type = models.CharField(max_length=100, verbose_name='نوع مشتری')
    date = models.DateField(verbose_name='تاریخ')
    distance_from_origin = models.FloatField(verbose_name='فاصله از مبدا')
    time_of_day = models.TimeField(verbose_name='زمان از روز')
    income = models.FloatField(default=0, verbose_name='درآمد سفر')

    def __str__(self):
        return self.courier.user.username + ' , ' + str(self.date) + ' , ' + str(self.income)

    class Meta:
        verbose_name = 'درآمد مربوط به یک سفر'


class CourierIncomeChange(models.Model):
    courier = models.ForeignKey(CourierProfile, on_delete=models.CASCADE)

    amount = models.FloatField(default=0, verbose_name='مقدار افزایش یا کاهش')
    date = models.DateField(verbose_name='تاریخ')

    def __str__(self):
        return self.courier.user.username + ' , ' + str(self.date) + ' , ' + str(self.amount)

    class Meta:
        verbose_name = 'کسر یا افزایش درآمد'


class CourierDailySalary(models.Model):
    courier = models.ForeignKey(CourierProfile, on_delete=models.CASCADE)

    date = models.DateField(verbose_name='تاریخ')
    daily_salary = models.FloatField(default=0, verbose_name='حقوق روزانه')

    def __str__(self):
        return self.courier.user.username + ' , ' + str(self.date) + ' , ' + str(self.daily_salary)

    class Meta:
        verbose_name = 'حقوق روزانه پیک'


class CourierWeeklySalary(models.Model):
    courier = models.ForeignKey(CourierProfile, on_delete=models.CASCADE)

    week_starting_date = models.DateField(verbose_name='شنبه هر هفته')
    weekly_salary = models.FloatField(default=0, verbose_name='حقوق هفتگی')

    def __str__(self):
        return self.courier.user.username + ' , ' + str(self.week_starting_date) + ' , ' + str(self.weekly_salary)

    class Meta:
        verbose_name = 'حقوق هفتگی پیک'
