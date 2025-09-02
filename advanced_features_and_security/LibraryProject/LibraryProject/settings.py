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
