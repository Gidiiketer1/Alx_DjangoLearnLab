# LibraryProject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'bookshelf',  # your custom app
]

# Use the custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# CSP settings using django-csp (install if needed)
INSTALLED_APPS += ['csp']
MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", 'data:')
