import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.api_base.settings")
django.setup()
