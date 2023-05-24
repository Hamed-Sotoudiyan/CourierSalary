from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'profileviewset', views.CourierProfileViewSet, basename="profileviewset")
router.register(r'tripviewset', views.TripViewSet, basename="tripviewset")
router.register(r'changeviewset', views.CourierIncomeChangeViewSet, basename="changeviewset")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/weeklylist/', views.CourierWeeklySalaryListView.as_view(), name="weeklylist"),
    path('api/dailylist/', views.CourierDailySalaryListView.as_view(), name="dailylist"),
]
