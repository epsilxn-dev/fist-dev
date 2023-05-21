import os
from datetime import timedelta
from pathlib import Path

import gspread
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
MAIN_DIR = BASE_DIR.parent

DEBUG = False if os.environ.get("MODE") == "PROD" else True

if DEBUG:
    load_dotenv(MAIN_DIR / ".env")

SECRET_KEY = os.environ.get("DJANGO_SECRET")

ENV_ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")
if ENV_ALLOWED_HOSTS:
    ALLOWED_HOSTS = ENV_ALLOWED_HOSTS.split(";")
else:
    ALLOWED_HOSTS = []

ROLES = [
    "user",
    "moderator",
    "admin"
]

INSTALLED_APPS = [
    # -----------------------------------------------
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'corsheaders',
    # -----------------------------------------------
    'tinymce',
    'filebrowser',
    # -----------------------------------------------
    'rest_framework',
    'src.modules.user.identification',
    'src.modules.tags',
    'src.modules.user.user',
    'src.modules.faculty.structure',
    'src.modules.faculty.laboratories',
    'src.modules.projects.ideas',
    'src.modules.work',
    'src.modules.questions',
    'src.modules.courses.north_valley',
    'src.modules.news.fac_news',
    'src.modules.courses.fist_school'
]

SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": 'src.core.utils.swagger.schema.MainSwaggerSchema'
}

TINYMCE_DEFAULT_CONFIG = {
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,searchreplace,visualblocks,code,"
               "fullscreen,insertdatetime,media,table,paste,",
    "height": 600,
    "toolbar": 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | '
               'bullist numlist outdent indent ',
    "paste_data_images": True,
    'file_browser_callback': 'mce_filebrowser'
}

# >> WYSIWYG
DIRECTORY = ''
FILEBROWSER_DIRECTORY = ''
# << WYSIWYG

X_FRAME_OPTIONS = 'SAMEORIGIN'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'src.core.utils.searching.paginator.Paginator',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'ordered_by',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "src.modules.user.identification.auth.AuthenticationSystem",
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter'
    ],
    'EXCEPTION_HANDLER': 'src.core.exception_receiver.err_handler'
}

JWT_ACCESS_LIFETIME = timedelta(minutes=10)
JWT_REFRESH_LIFETIME = timedelta(days=7)

HOST_DOMAIN = "http://127.0.0.1:3000" if DEBUG else os.environ.get("HOST_DOMAIN")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'src.middlewares.high_level_data.DataMiddleware'
]

APPEND_SLASH = True

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:3000"]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
],

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = "user.Person"

if DEBUG:
    BASE_DOMAIN = "127.0.0.1"
    BASE_PORT = ":3000"
    BASE_PROTOCOL = "http"
else:
    BASE_DOMAIN = os.environ.get("HOSTING_HOST")
    BASE_PORT = ""
    BASE_PROTOCOL = os.environ.get("HOSTING_PROTOCOL")

try:
    NORTH_VALLEY_SHEET_NAME = os.environ.get("NORTH_VALLEY_SHEET_NAME")
    GSPREAD_CLIENT = gspread.service_account(filename=str(BASE_DIR / "service_account.json"))
except FileNotFoundError as e:
    ...

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

FILE_UPLOAD_MAX_MEMORY_SIZE = 8388608
FIRST_DAY_OF_WEEK = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
