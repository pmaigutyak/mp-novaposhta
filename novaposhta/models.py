
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Warehouse(models.Model):

    title = models.CharField(_('Title'), max_length=255, db_index=True)

    address = models.CharField(_('Address'), max_length=255, db_index=True)

    @property
    def full_name(self):
        return '{}, {}'.format(self.title, self.address)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Warehouse')
        verbose_name_plural = _('Warehouses')
