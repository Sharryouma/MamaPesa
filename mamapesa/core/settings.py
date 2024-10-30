"""
Django settings for project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_HOST_USER="sammymaiko721@gmail.com"
EMAIL_HOST_PASSWORD="edcy kafn qnjj htak"
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0q!p3()$p35u=gsr+k=ta+smp2klfilu%m)*5w1deefit%^t^o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'savingsandloans',
    'tailwind',  
    'theme',
    'django_browser_reload',
    'corsheaders',
    
    # 'mpesa_api',
    
]

TAILWIND_APP_NAME='theme'

NODEJS_BIN_PATH = '/c/Install/node'
NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    "django.middleware.common.CommonMiddleware",
]

# examples
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
# CORS_ALLOWED_ORIGINS = [
#    "https://example.com",
#   "https://sub.example.com",
#   "http://127.0.0.1:9000",
#

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql',
#     #     'NAME': 'railway',
#     #     'USER': 'postgres',
#     #     'PASSWORD': '1cdA3E2A3bccbcDegEEbbgbe1b6dC552',
#     #     'HOST': 'viaduct.proxy.rlwy.net',
#     #     'PORT': '22761',
#     # }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'accounts.backends.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'Mamapesa__media'

AUTH_USER_MODEL='accounts.CustomUser'

REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':(
      'rest_framework.authentication.TokenAuthentication',
    ),
}


