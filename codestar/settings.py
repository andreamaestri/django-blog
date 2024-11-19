"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os

import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Loading variables from .env file
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# Check if running on Heroku
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

# Use environment variable for DEBUG setting
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# For development, you can override this in your local .env file
# DEBUG=True

# For Heroku production, make sure DEBUG is False
# heroku config:set DEBUG=False

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # Add WhiteNoise
    "admin_interface",
    "colorfield",
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'about',
    'tinymce',
    'compressor',
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add WhiteNoise middleware
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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
TINYMCE_JS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/tinymce/7.5.1/tinymce.min.js'
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "width": "100%",
    "height": "600px",
    "menubar": "file edit view insert format tools help",
    "skin": "oxide-dark",
    "content_css": "dark",
    "plugins": (
        "advlist autolink lists link image charmap preview anchor "
        "searchreplace visualblocks code fullscreen "
        "insertdatetime media table paste code help wordcount "
        "codesample quickbars emoticons"
    ),
    "toolbar": (
        "undo redo | blocks | bold italic backcolor | "
        "alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | codesample | "
        "removeformat | help | code | link image media table | "
        "visualblocks fullscreen preview"
    ),
    "codesample_global_prismjs": True,
    "codesample_languages": [
        {"text": "Python", "value": "python"},
        {"text": "JavaScript", "value": "javascript"},
        {"text": "HTML/XML", "value": "markup"},
        {"text": "CSS", "value": "css"},
        {"text": "TypeScript", "value": "typescript"},
        {"text": "Java", "value": "java"},
        {"text": "C#", "value": "csharp"},
        {"text": "PHP", "value": "php"},
        {"text": "Ruby", "value": "ruby"},
        {"text": "SQL", "value": "sql"},
        {"text": "Bash", "value": "bash"},
        {"text": "Git", "value": "git"}
    ],
    "toolbar_mode": "sliding",
    "contextmenu": "link image table codesample",
    "quickbars_selection_toolbar": "bold italic | quicklink h2 h3 blockquote codesample",
    "content_style": "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; line-height: 1.6; }",
}

WSGI_APPLICATION = 'codestar.wsgi.application'

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

# Database
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(),
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# WhiteNoise configuration
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
WHITENOISE_KEEP_ONLY_HASHED_FILES = True
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if not DEBUG:
    # Security settings for production
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Improved error logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    }
