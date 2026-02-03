import os
from pathlib import Path

# ===========================
# BASE DIR
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-!3k&*l4f#@r$2q9z1p0v^5t+8w7y6x0b"

# ===========================
# DEBUG & HOSTS
# ===========================
DEBUG = True
ALLOWED_HOSTS = []

# ===========================
# APPS INSTALADAS
# ===========================
INSTALLED_APPS = [
    # Django padrão
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'rest_framework',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Seus apps
    'apps.characters.apps.CharactersConfig',
    # 'apps.users.apps.UsersConfig',
    # 'apps.posts.apps.PostsConfig',
]

# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',           # obrigatório
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',        # obrigatório
    'django.contrib.messages.middleware.MessageMiddleware',           # obrigatório
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# URL CONFIG
# ===========================
ROOT_URLCONF = 'config.urls'


# ===========================
# TEMPLATES
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # obrigatório
        'DIRS': [BASE_DIR / 'templates'],  # se tiver templates globais
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ===========================
# WSGI
# ===========================
WSGI_APPLICATION = 'config.wsgi.application'

# ===========================
# DATABASE (exemplo SQLite)
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================
# PASSWORD VALIDATION
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ===========================
# INTERNATIONALIZATION
# ===========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===========================
# STATIC FILES
# ===========================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# ===========================
# MEDIA FILES
# ===========================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ===========================
# DEFAULT AUTO FIELD
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

