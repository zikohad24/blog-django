
# 📝 Blog Django · My Site

Aquest és un projecte de blog desenvolupat amb Django com a part de l'assignatura **M3 - UF6**.

## 🧩 Funcionalitats

- Llistat de posts amb títol, imatge i fragment de text.
- Detall de cada post amb contingut complet.
- Autors amb les seves dades i llistat dels seus posts.
- Etiquetes (tags) associades a cada post.
- Filtres de posts per tag.
- Dades carregades des de fixtures (`initial_data.json`).
- Ús de Bootstrap 5 per al disseny visual.

## 📁 Estructura del projecte

```
my_site/
├── blog/
│   ├── migrations/
│   ├── static/blog/img/
│   ├── templates/blog/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── fixtures/initial_data.json
├── my_site/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
└── manage.py
```

## 🚀 Execució local

1. Crea i activa un entorn virtual:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate a Windows
```

2. Instal·la les dependències:

```bash
pip install -r requirements.txt
```

3. Aplica les migracions i carrega dades:

```bash
python manage.py migrate
python manage.py loaddata initial_data.json
```

4. Executa el servidor:

```bash
python manage.py runserver
```

## 🧪 Tests i Accions

- S’han implementat tests automàtics per a models (Author, Tag, Post).
- Hi ha una **GitHub Action** per comprovar que els tests funcionen.
- També es genera automàticament la documentació amb `pydoc` i es publica a GitHub Pages.

## 📚 Documentació amb Pydoc

➡️ [Veure documentació Pydoc generada](https://zikohad24.github.io/blog-django/blog.models.html)

---

## 🔗 Crèdits

Projecte creat com a part de l’assignatura **M3 - UF6** de cicles formatius.
