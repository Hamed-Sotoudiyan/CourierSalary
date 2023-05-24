from rest_framework import serializers

from .models import CourierWeeklySalary, CourierProfile, CourierDailySalary, CourierIncomeChange, Trip


class CourierProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierProfile
        fields = '__all__'


class CourierWeeklySalarySerializer(serializers.ModelSerializer):
    courier = CourierProfileSerializer(many=False, read_only=True)

    class Meta:
        model = CourierWeeklySalary
        fields = ['weekly_salary', 'courier', 'week_starting_date']


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['distance',
                  'courier',
                  'customer_type',
                  'date',
                  'distance_from_origin',
                  'time_of_day',
                  'income']


class CourierIncomeChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierIncomeChange
        fields = ['courier', 'amount', 'date']


class CourierDailySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierDailySalary
        fields = ['courier', 'date', 'daily_salary']
