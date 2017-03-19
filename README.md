# MP-Novaposhta

Django nova poshta ua api app.

### Installation

Install with pip:

```sh
$ pip install django-novaposhta
```

Add novaposhta to urls.py:

```
urlpatterns += i18n_patterns(
    url(r'^nova-poshta/', include('novaposhta.urls', namespace='nova-poshta')),
)
```

Add novaposhta to settings.py:
```
INSTALLED_APPS = [
    'novaposhta',
]
```

Run migrations:
```
$ python manage.py migrate
```

### Requirements

App require this packages:

* django-model-search
