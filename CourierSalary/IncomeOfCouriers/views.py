from datetime import datetime

from rest_framework import generics, filters
from rest_framework import viewsets

from .models import Trip, CourierIncomeChange, CourierDailySalary, CourierProfile, CourierWeeklySalary
from .serializers import CourierProfileSerializer, CourierWeeklySalarySerializer, TripSerializer, \
    CourierIncomeChangeSerializer, CourierDailySalarySerializer


class CourierWeeklySalaryListView(generics.ListAPIView):
    serializer_class = CourierWeeklySalarySerializer
    queryset = CourierWeeklySalary.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['week_starting_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        date_from_str = self.request.query_params.get('from_date')
        date_to_str = self.request.query_params.get('to_date')

        if date_from_str and date_to_str:
            from_date = datetime.strptime(date_from_str, "%Y-%m-%d").date()
            to_date = datetime.strptime(date_to_str, "%Y-%m-%d").date()
            queryset = queryset.filter(week_starting_date=[from_date, to_date])

        return queryset


class CourierDailySalaryListView(generics.ListAPIView):
    serializer_class = CourierDailySalarySerializer
    queryset = CourierDailySalary.objects.all()


class CourierProfileViewSet(viewsets.ModelViewSet):
    queryset = CourierProfile.objects.all()
    serializer_class = CourierProfileSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class CourierIncomeChangeViewSet(viewsets.ModelViewSet):
    queryset = CourierIncomeChange.objects.all()
    serializer_class = CourierIncomeChangeSerializer
