# MP-Novaposhta

Django nova poshta ua api app.

### Installation

1) Install with pip:

```
pip install django-novaposhta
```

2) Add app to urls.py:

```
path('novaposhta/', include('novaposhta.urls')),
```

3) Add `novaposhta` to INSTALLED_APPS

4) Add `NOVA_POSHTA_API_KEY` to your settings.py

5) Run `python manage.py migrate`

### Refresh warehouses
To refresh warehouses you should login as staff and visit
`/novaposhta/refresh` url.
Old warehouse records will be removed.

### Requirements

App require this packages:

* django-model-search
