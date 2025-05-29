# generate_docs.py
import os
import django
import pydoc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

pydoc.writedoc("blog.models")
pydoc.writedoc("blog.urls")
