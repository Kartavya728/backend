# portfolio_project/settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE PRODUCTION SETTINGS
# ==============================================================================

# SECURITY WARNING: The secret key is now loaded from an environment variable.
# You MUST set this variable on your PythonAnywhere server.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default-insecure-key-for-local-dev-only')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# You MUST replace 'your-username' with your actual PythonAnywhere username.
# This tells Django which domain is allowed to serve your site.
ALLOWED_HOSTS = ['your-username.pythonanywhere.com']


# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'


# ==============================================================================
# DATABASE
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# STATIC & MEDIA FILES (For CSS, JS, and User-Uploaded Images)
# ==============================================================================

# The URL to access static files (CSS, JavaScript, etc.)
STATIC_URL = 'static/'
# The absolute path where 'collectstatic' will gather all static files for production.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to access user-uploaded files (like your project images).
MEDIA_URL = '/media/'
# The absolute path to the folder where user-uploaded files will be stored.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = [
    'kartavya728.pythonanywhere.com', 
    '127.0.0.1',
    'localhost',
]
# ==============================================================================
# CORS (Cross-Origin Resource Sharing) SETTINGS
# =================================================CORS_ALLOW_ALL_ORIGINS = True
# For production, it's more secure to specify allowed origins.
# You will get this from Vercel or wherever your frontend is hosted.
# settings.py

# This will allow requests from localhost, your Vercel domains,
# your Cloudflare Pages domains, and any other domain.
CORS_ALLOW_ALL_ORIGINS = True

# ==============================================================================
# OTHER SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'