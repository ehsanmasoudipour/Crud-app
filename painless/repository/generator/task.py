from typing import List
from mimesis.locales import Locale
from mimesis import (
    Text,
    Person,
    Numeric,
)

class BaseDataGenerator:
    def __init__(self, locale='en'):
        self.text = Text(getattr(Locale, locale.upper()))
    
    def get_random_words(self, total):
        words = self.text.words(quantity=total)
        return ' '.join(words)
    
    def get_random_sentence(self, total):
        return self.text.text(quantity = total)