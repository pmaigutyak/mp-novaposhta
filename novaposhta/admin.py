
from django.contrib import admin

from novaposhta.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):

    list_display = ('title', 'address', )
    search_fields = ('title', 'address', )

admin.site.register(Warehouse, WarehouseAdmin)