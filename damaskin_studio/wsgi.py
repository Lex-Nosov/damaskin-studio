"""
WSGI config for damaskin_studio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'damaskin_studio.settings')

application = get_wsgi_application()


def square_digits(num):
    total = []
    for i in list(str(num)):
        total.append(int(i)**2)
    return ''.join(total)


print(square_digits(9119))
