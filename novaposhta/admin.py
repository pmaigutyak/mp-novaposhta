
from django.contrib import admin

from novaposhta.models import Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = ('title', 'address', )
    search_fields = ('title', 'address', )
