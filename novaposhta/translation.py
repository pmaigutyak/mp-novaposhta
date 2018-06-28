
from modeltranslation.translator import translator

from novaposhta.models import Warehouse


translator.register(Warehouse, fields=['title', 'address'])
