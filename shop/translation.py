from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Food)
class ProductTranslationOptions(TranslationOptions):
    fields = ('resto_name', 'description')