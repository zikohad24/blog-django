# generate_docs.py

import os
import django
import pydoc

# Configura les variables d'entorn per a Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

# Llista de mòduls que vols documentar
modules_to_doc = [
    "blog.models",
    "blog.urls",
]

# Genera els fitxers HTML a la carpeta actual
for module in modules_to_doc:
    pydoc.writedoc(module)
