from kernel.settings.base import DEFAULT_APPS

THIRD_PARTY_APPS = [
    'rest_framework',
]
BUSINESS_APPS = [
    'warehouse',
    'account',
]
INSTALLED_APPS = DEFAULT_APPS + BUSINESS_APPS + THIRD_PARTY_APPS
