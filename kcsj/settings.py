#coding=utf-8
"""
Django settings for kcsj project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'if4s&rsp65^oe*o!%%e*(%x9*pxazr0&bae%+&50a*cer$a(xa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True and 'VIRTUALENVWRAPPER_PROJECT_FILENAME' not in os.environ
    
ALLOWED_HOSTS = [
        "localhost",'127.0.0.1',
        'williezheng.pythonanywhere.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DJangoHotel',
    'qiniuyun',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kcsj.urls'

WSGI_APPLICATION = 'kcsj.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')] ,
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

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if 1:
    from local_settings import email_conf,qiniu_conf,DATABASES as local_db
    DATABASES = local_db    
    
# qiniu settigs for upload used by 'qiniuyun.QiniuPush'
# https://github.com/qiniu/python-sdk
    
    QINIU_CONF=qiniu_conf
#  ---------------------------------------------------------    
#  Email ,ref:http://www.cnblogs.com/BeginMan/p/3443158.html
    EMAIL_BACKEND = email_conf["EMAIL_BACKEND"]
 
    EMAIL_USE_TLS = email_conf["EMAIL_USE_TLS"]
    EMAIL_HOST = email_conf["EMAIL_HOST"]
    EMAIL_PORT = email_conf["EMAIL_PORT"]
    EMAIL_HOST_USER = email_conf["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = email_conf["EMAIL_HOST_PASSWORD"]
    DEFAULT_FROM_EMAIL = email_conf["DEFAULT_FROM_EMAIL"]
#  ---------------------------------------------------------

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),

)
