"""
Configurações do projeto Django 'config'.

Gerado com 'django-admin startproject' usando Django 5.2.4.

Documentação:
- Visão geral: https://docs.djangoproject.com/en/5.2/topics/settings/
- Lista completa: https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta (NUNCA exponha em produção)
SECRET_KEY = 'django-insecure-5qa*(+0@#z4ke^k6+rp=!-o#@8!o7o*c)i=5%2@$nvqbwzlx4n'

# Debug deve estar em False em produção
DEBUG = False

# Lista de hosts permitidos (em produção, defina os domínios/IPs)
ALLOWED_HOSTS = ['jgluciano.pythonanywhere.com']

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sistema',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração de URLs
ROOT_URLCONF = 'config.urls'

# Configuração de Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Coloque aqui os caminhos adicionais para templates, se necessário
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicação WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Banco de Dados (padrão: SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validações de senha
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

# Internacionalização
LANGUAGE_CODE = 'en-us'   # ou 'pt-br' se preferir em português
TIME_ZONE = 'UTC'         # ou 'America/Sao_Paulo' para horário do Brasil
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JS, imagens)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tipo padrão de chave primária para novos modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
