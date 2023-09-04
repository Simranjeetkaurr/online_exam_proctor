from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

FILES = os.path.join(BASE_DIR, 'frontend')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-kyh8ne^tm-n9jk#4_5(6nddqlc-nxe3+^@uutgzlwu$hn&2n=3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "questions",
    "student",
    "teacher",
    "bootstrap4"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'support_app.middleware.SystemCheckMiddleware',

]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(FILES, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": "mssql",
#         "NAME": "CU_LMS_Dev",
#         "USER": "sa",
#         "HOST": "3.109.95.156",
#         "PORT": "1433",
#         "PASSWORD": "Test@123",
#         "OPTIONS": {
#             "driver": "ODBC Driver 17 for SQL Server",
#         }
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "CU_LMS_Dev",
        "USER": "sa",
        "HOST": "3.109.95.156",
        "PORT": "1433",
        "PASSWORD": "Test@123",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server"
        }
         
    }
} 

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = False


STATIC_ROOT = os.path.join(FILES, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(FILES, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(FILES, 'assets')]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SUPPORTED_PARAMETERS = {
#     'operating_system': ['Windows 7', 'Windows 8', 'Windows 8.1', 'Windows 10', 'Mac OS X: MacOS 10.10', '10.11', '10.12', '10.13(OS X)'],
#     'supported_devices': ['Desktop', 'Laptop*'],
#     'processor': '64-bit Intel® Pentium 4 processor or later that’s SSE2 capable',
#     'memory': '4 GB RAM',
#     'screen_size': '14 inch',
#     'screen_resolution': '1024 x 768 24 bit',
#     'other_requirements': 'External keyboard and mouse, Wired network connection required, Broadband internet 5MB/s download, 1 MB/s upload per examinee workstation (minimum 10MB/s download and 5MB/s upload)',
# }

