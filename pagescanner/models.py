from django.db import models
from dashboards.models import Dashboard


class Scan(models.Model):
    started_datetime = models.DateTimeField(auto_now=True)
    finish_datetime = models.DateTimeField()
    dashboard = models.ForeignKey(Dashboard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.dashboard.name
