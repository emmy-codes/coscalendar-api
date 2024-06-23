from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

if os.path.exists("env.py"):
    import env


CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL")
}

MEDIA_URL = "/media/"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication" 
  ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DATETIME_FORMAT": "%d-%m-%Y",
    # defaults
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

# exclude BrowsableAPIRenderer in production
if "DEV" in os.environ:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )

REST_AUTH = {
    "USE_JWT": True,  
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    # Configure the domain and path of the cookie
    'JWT_AUTH_COOKIE_DOMAIN': None,  
    'JWT_AUTH_COOKIE_PATH': '/',     
    
    # Security settings
    'JWT_AUTH_HTTPONLY': True,  
    'JWT_AUTH_SAMESITE': 'None', 
    'JWT_AUTH_SECURE': True,   
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'coscalendar_api.serializers.CurrentUserSerializer',
    'TOKEN_SERIALIZER': 'dj_rest_auth.utils.JWTCookieAuthentication',  # noqa
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    os.environ.get("ALLOWED_HOST"),
    "localhost",
    "127.0.0.1",
    "coscalendar-api-3bdc9b15f518.herokuapp.com"
    ]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",

    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    
    "django.contrib.sites",
    
    "dj_rest_auth.registration",
    "dj_rest_auth",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    
    "corsheaders",
    
    "user_profiles",
    "cosplans",
    "cosexpenses",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "https://coscalendar-api-3bdc9b15f518.herokuapp.com",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://127.0.0.1:\d+$",    
    r"^http://localhost:\d+$",
    r"https://coscalendar-api-3bdc9b15f518.herokuapp.com/",
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = "coscalendar_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "coscalendar_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "DEV" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]

# force reformatting date format to match frontend

USE_L10N = False

DATE_FORMAT = "d-m-Y"

DATE_INPUT_FORMATS = [
    "%d-%m-%Y",
    "%Y-%m-%d"
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
