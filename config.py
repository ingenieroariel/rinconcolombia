from satchmo.configuration import config_get

LANGUAGES_AVAILABLE = config_get('LANGUAGE', 'LANGUAGES_AVAILABLE')

LANGUAGES_AVAILABLE.add_choice(('es', 'Spanish'))
