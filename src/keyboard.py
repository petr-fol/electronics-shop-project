from src.item import Item  # Подключаем базовый класс Item


class KeyboardMixin:
    def __init__(self, language):
        self.language = language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_language):
        if new_language in ['EN', 'RU']:
            self._language = new_language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, KeyboardMixin):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        KeyboardMixin.__init__(self, language)
