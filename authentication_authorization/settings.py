"""
2:09:42
Django WP ADMIN ____ CHECK  !
authorization: what you can do?
authentication: who you are? how you prove it(credentials)?
identification: the ability to identify uniquely a user of a system or an application that is running in the system.
                the system uses username to identify the user.
single-factor authentication:
multi-factor authentication:
last-pass: application for password management
Oauth 2.0 and JSON Web Tokens: useful for client-side rendering, not SSR
authentication in Django(consists of...):
- users
- groups
- permissions(roles)

- a configurable hashing system
- it handles cookie-based sessions
- what can you include in session? - last 3 viewed items

user: an individual accessing a website through a web browser.
    In Django the user objects are the core of the authentication system.

WEB SECURITY:
- SQL Injection: someone can insert information in our application. In order to protect ourselves we use ORM
- Cross-site Scripting(XSS): similar to above, asking people to click bad things on our site through JS injection
- URL/HTTP manipulation attacks(Parameter Tampering): change params in the URL. Only problem if we do not validate access
- Cross-site Request Forgery(CSRF): we click on something without wanting to click on it
- Brute Force Attacks (also DDoS): too many requests to our site and the site stops working => unhappy customers
- Insufficient Access Control
- Missing SSL(HTTPS)/MITM
- Phishing/Social Engineering: someone else sending email from our side with 'click here' to change pass

pip install bleach - additional package to sanitize our HTML
check config for google login
"""

from pathlib import Path

from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8+nzl=id@n-(_lk85)^((idny1500(w5q^d2&j9f9bj-_s5h!_'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authentication_authorization.web',
    'authentication_authorization.auth_app',
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

ROOT_URLCONF = 'authentication_authorization.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'authentication_authorization.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#WRITE IT ONLY HERE, IN SETTINGS.PY
LOGIN_URL = reverse_lazy('sign in')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
AUTH_USER_MODEL = 'auth_app.AppUser'
