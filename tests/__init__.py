import os
import sys

import django

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tekey.settings")
django.setup()
