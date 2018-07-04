"# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Unipath aqui
from unipath import Path
BASE_DIR = Path(__file__).parent

...
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'cadastro',
)
...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': BASE_DIR.child('db.sqlite3'), # Unipath aqui
    }
}

LANGUAGE_CODE = 'pt-br'