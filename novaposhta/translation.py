
from modeltranslation.translator import register, TranslationOptions

from novaposhta.models import Warehouse


@register(Warehouse)
class WarehouseTranslationOptions(TranslationOptions):

    fields = ('title', 'address', )
