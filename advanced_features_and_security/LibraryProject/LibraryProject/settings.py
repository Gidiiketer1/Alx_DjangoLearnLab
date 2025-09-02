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
# Redirects all HTTP requests to HTTPS for secure communication
SECURE_SSL_REDIRECT = True

# Instruct browsers to use HTTPS only for the next 1 year (HSTS)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow inclusion in browser preload lists

# Cookies only transmitted over HTTPS for session and CSRF protection
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent clickjacking by disallowing framing of the site
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME-type sniffing to reduce attack surface
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser's XSS filtering for extra protection
SECURE_BROWSER_XSS_FILTER = True
# Detect HTTPS requests properly when behind a proxy/load balancer
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
