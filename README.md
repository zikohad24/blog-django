# 📝 Blog Django · My Site

Aquest és un projecte de blog desenvolupat amb Django com a part de l'assignatura **M3 - UF6**.

---

## 🧩 Funcionalitats

- Llistat de posts amb títol, imatge i fragment de text.
- Detall de cada post amb contingut complet.
- Autors amb les seves dades i llistat dels seus posts.
- Etiquetes (tags) associades a cada post.
- Filtres de posts per tag.
- Dades carregades des de fixtures (`initial_data.json`).
- Ús de **Bootstrap 5** per al disseny visual.

---

## 📁 Estructura del projecte

my_site/
├── blog/
│ ├── migrations/
│ ├── static/blog/img/
│ ├── templates/blog/
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── fixtures/initial_data.json
├── my_site/
│ ├── settings.py
│ └── urls.py
├── db.sqlite3
└── manage.py


---

## 🚀 Execució local

1. **Crea i activa un entorn virtual:**

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate a Windows
Instal·la les dependències:

bash
Copier
Modifier
pip install -r requirements.txt
Aplica les migracions i carrega dades:

bash
Copier
Modifier
python manage.py migrate
python manage.py loaddata initial_data.json
Executa el servidor:

bash
Copier
Modifier
python manage.py runserver
🔗 Crèdits
Projecte creat com a part de l’assignatura M3 - UF6 de cicles formatius.

yaml
Copier
Modifier

---

### 🔧 Vols que t’ajudi ara a:

- Crear el fitxer `requirements.txt`?
- Pujar-lo a GitHub?
- Afegir una demo visual (captura de pantalla al README)?

Només digues "sí" i t’ho preparo tot.







