# Connectin | Spice Assignmet

## How to run project ?

**Install redis and run it before running the project**

```shell
$ pip3 install -r requirements.txt

$ cd connectin

$ python3 manage.py makemigrations
$ python3 manage.py migrate

$ python3 manage.py runserver

```

*In another shell*
```shell
$ celery -A connectin worker -l info
```
