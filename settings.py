import os.path
import pickle

DEFAULT_FONT_SIZE = 24
DEFAULT_FONT_NAME = 'UbuntuMono-R.ttf'
DEFAULT_LANGUAGE = 'en'

SETTINGS_PATH = 'DATA\\settings.pickle'
LOCALIZATION_PATH_START_SYMBOLS = 'DATA\\localization\\en-'
LOCALIZATION_PATH_LAST_SYMBOLS = '.txt'
MIN_FONT_SIZE = 8
MAX_FONT_SIZE = 40


class Settings:

    def __init__(self):
        self.font_size = DEFAULT_FONT_SIZE
        self.font_name = DEFAULT_FONT_NAME
        self.language = DEFAULT_LANGUAGE
        self._set_saved_settings()

    def set_font_size(self, new_font_size):
        if self._new_font_size_is_correct(new_font_size):
            self.font_size = new_font_size
            self._save()

    def set_font_name(self, new_font_name):
        if self._new_font_name_is_correct(new_font_name):
            self.font_name = new_font_name
            self._save()

    def set_language(self, new_language):
        if self._new_language_path_is_correct(new_language):
            self.language = new_language
            self._save()

    def _set_saved_settings(self):
        if self._new_settings_path_is_correct(SETTINGS_PATH):
            new_settings = self._load_settings()
            self._update(new_settings)

    def _save(self):
        f = open(SETTINGS_PATH, 'wb')
        pickle.dump(self, f)
        f.close()

    @staticmethod
    def _load_settings():
        f = open(SETTINGS_PATH, 'rb')
        new_settings = pickle.load(f)
        f.close()
        return new_settings

    def _update(self, new_settings):
        new_font_size = new_settings.font_size
        new_font_name = new_settings.font_name
        new_language = new_settings.language
        self.set_font_size(new_font_size)
        self.set_font_name(new_font_name)
        self.set_language(new_language)

    @staticmethod
    def _new_settings_path_is_correct(settings_path):
        if type(settings_path) is not str:
            return False
        return os.path.isfile(settings_path)

    @staticmethod
    def _new_font_size_is_correct(new_font_size):
        if type(new_font_size) is not int:
            return False
        if not (MIN_FONT_SIZE < new_font_size < MAX_FONT_SIZE):
            return False
        return True

    @staticmethod
    def _new_font_name_is_correct(new_font_name):
        if type(new_font_name) is not str:
            return False
        return os.path.isfile(new_font_name)

    @staticmethod
    def _new_language_path_is_correct(new_language):
        if type(new_language) is not str:
            return False
        new_language_path = LOCALIZATION_PATH_START_SYMBOLS + new_language + LOCALIZATION_PATH_LAST_SYMBOLS
        print(new_language_path)
        return os.path.isfile(new_language_path)

    def _load_defaults(self):
        self.font_size = DEFAULT_FONT_SIZE
        self.font_name = DEFAULT_FONT_NAME
        self.language = DEFAULT_LANGUAGE
        self._save()


current_settings = Settings()
