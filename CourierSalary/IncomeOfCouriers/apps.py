from django.apps import AppConfig


class IncomeOfCouriersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IncomeOfCouriers'

    def ready(self):
        # Import signal handlers
        from . import signals

