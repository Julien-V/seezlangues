"""
Django settings for seezlangues project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'seezlangues.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'seezlangues.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher'
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

##############################################
# Seezlangues settings : app_blog            #
##############################################

""" a_category = {
    "name": <str:cat_name>,
    "group": <str:cat_group> or None
    "sub_cat": list(dict) or None
}
"""
APP_BLOG_CATEGORY_HIERARCHY = [
    {
        "name": 'Langues',
        "group": None,
        "sub_cat": [
            dict(name=x[0], group=x[1], sub_cat=x[2]) for x in [
                ['Anglais', None, None],
                ['Espagnol', None, None],
                ['Allemand', None, None],
                ['Italien', None, None],
                ['Russe', None, None]]
            ]
    }, {
        "name": 'Ressources',
        "group": None,
        "sub_cat": [
            dict(name=x[0], group=x[1], sub_cat=x[2]) for x in [
                ['Ressources non didactisées libres', None, None],
                ['Ressources didactisées', "Contributeur", None],
                ["Productions d'Élèves", "Auteur", None]]
            ]
    }, {
        "name": 'Outils Numériques',
        "group": None,
        "sub_cat": [
            dict(name=x[0], group=x[1], sub_cat=x[2]) for x in [
                ['Le Numérique', None, None],
                ['Tutoriels', "Auteur", None]]
            ]
    }, {
        "name": 'Salle des professeurs',
        "group": None,
        "sub_cat": [
            dict(name=x[0], group=x[1], sub_cat=x[2]) for x in [
                ['Référentiels', None, None],
                ["Paroles d'IPR", 'Auteur', None],
                ["Forum", "Auteur", None],
                ["Conseiller", "Conseiller", None]]
            ]
    }, {
        "name": 'Agenda',
        "group": None,
        "sub_cat": [
            dict(name=x[0], group=x[1], sub_cat=x[2]) for x in [
                ['Formations', "Contributeur", None],
                ['Évènements', None, None]]
            ]
    }
]
