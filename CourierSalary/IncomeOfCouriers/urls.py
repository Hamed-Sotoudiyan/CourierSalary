from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'profile-viewset', views.CourierProfileViewSet, basename="profile-viewset")
router.register(r'trip-viewset', views.TripViewSet, basename="trip-viewset")
router.register(r'change-viewset', views.CourierIncomeChangeViewSet, basename="change-viewset")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-list/weekly/', views.CourierWeeklySalaryListView.as_view(), name="weeklylist"),
    path('api-list/daily/', views.CourierDailySalaryListView.as_view(), name="dailylist"),
]
