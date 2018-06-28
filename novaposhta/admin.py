
from importlib import import_module

from django.apps import apps
from django.contrib import admin

from novaposhta.models import Warehouse


def _get_warehouse_admin_base_class():

    if apps.is_installed('modeltranslation'):
        return import_module('modeltranslation.admin').TranslationAdmin

    return admin.ModelAdmin


class WarehouseAdmin(_get_warehouse_admin_base_class()):

    list_display = ['title', 'address']
    search_fields = ['title', 'address']


admin.site.register(Warehouse, WarehouseAdmin)
