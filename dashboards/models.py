from django.db import models
from octoscan.settings import AUTH_USER_MODEL


class Dashboard(models.Model):

    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='dashboards',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, blank=False)
    url = models.URLField(unique=True, blank=False)

    def __str__(self):
        return '%d - %s' % (self.id, self.name)


class PageModel(models.Model):
    url = models.URLField(blank=False)
    dashboard = models.ForeignKey(Dashboard, related_name='pages',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return '%d - %s' % (self.id, self.url)
